import sys
import json
import re


CATEGORY_KEYWORDS = {
    "billing": ["charged", "charge", "payment", "refund", "invoice", "subscription", "paid", "billing"],
    "bug": ["bug", "error", "crash", "crashed", "broken", "failed", "failure", "not working", "glitch"],
    "account issue": ["login", "log in", "password", "account", "locked", "sign in", "access"],
    "feature request": ["feature", "request", "suggest", "would like", "improve", "add", "enhancement"],
}

URGENCY_KEYWORDS = [
    "urgent", "immediately", "angry", "cancel", "legal", "lawsuit",
    "asap", "unacceptable", "terrible", "cannot use", "blocked"
]


def clean_text(text):
    return text.lower().strip()


def count_matches(text, keywords):
    count = 0
    matched = []

    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword) + r"\b"
        if re.search(pattern, text):
            count += 1
            matched.append(keyword)

    return count, matched


def classify_ticket(ticket_text):
    text = clean_text(ticket_text)

    # too short → uncertain
    if len(text.split()) < 5:
        return {
            "category": "uncertain",
            "priority": "low",
            "escalation": "no",
            "reason": "The ticket is too short or vague to classify reliably.",
            "matched_categories": [],
            "matched_keywords": []
        }

    scores = {}
    matched_keywords = {}

    for category, keywords in CATEGORY_KEYWORDS.items():
        score, matched = count_matches(text, keywords)
        scores[category] = score
        matched_keywords[category] = matched

    # find the best
    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        best_category = "other"

    # for edge case
    all_matched_categories = [
        category for category, score in scores.items() if score > 0
    ]

    # urgency
    urgency_score, urgency_matches = count_matches(text, URGENCY_KEYWORDS)

    # improvement
    if urgency_score >= 2 or len(all_matched_categories) >= 2:
        priority = "high"
        escalation = "yes"
    elif urgency_score == 1 or best_category in ["billing", "bug", "account issue"]:
        priority = "medium"
        escalation = "yes" if best_category in ["billing", "bug", "account issue"] else "no"
    else:
        priority = "low"
        escalation = "no"

    # reason
    reason_parts = []

    if best_category != "other":
        reason_parts.append(f"Detected category signals for {best_category}.")
    else:
        reason_parts.append("No strong category-specific keywords were detected.")

    if urgency_matches:
        reason_parts.append(f"Urgency signals detected: {', '.join(urgency_matches)}.")

    if len(all_matched_categories) >= 2:
        reason_parts.append(f"Multiple issue types detected: {', '.join(all_matched_categories)}.")

    return {
        "category": best_category,
        "priority": priority,
        "escalation": escalation,
        "reason": " ".join(reason_parts),
        "matched_categories": all_matched_categories,
        "matched_keywords": matched_keywords.get(best_category, []) + urgency_matches
    }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ticket_text = " ".join(sys.argv[1:])
    else:
        ticket_text = sys.stdin.read()

    result = classify_ticket(ticket_text)
    print(json.dumps(result, indent=2))