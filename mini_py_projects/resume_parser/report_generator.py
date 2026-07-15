try:
    from .matcher import matched_resume
except ImportError:
    from matcher import matched_resume


def report(result):
    print("Candidate Information")
    print("- Name:", result.get("personal_info", {}).get("name"))
    print("- Email:", result.get("personal_info", {}).get("email"))
    print("- Phone:", result.get("personal_info", {}).get("phone"))

    print("===============================")
    print("Overall Score:", result.get("score"))
    print("Summary:", result.get("summary"))

    print("\nStrengths:")
    for item in result.get("strengths", []):
        print("-", item)

    print("\nWeaknesses:")
    for item in result.get("weaknesses", []):
        print("-", item)

    print("\nMissing Fields:")
    for item in result.get("missing_fields", []):
        print("-", item)

    print("\nFeedback:")
    print(result.get("feedback", ""))
    print("============= END ==============")
