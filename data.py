# data.py  -- single source of truth for facts (DRY principle)

FATALITY_STATS = {
    "india": {
        "deaths_2015": 146133,
        "deaths_2025": 183382,
        "deaths_per_hour_2025": 21,
        "fatality_rate_per_100k": 16.2,
        "source": "TOI editorial 'Sense & Licence'; WHO rate cited in article",
    },
    "vietnam": {
        "licence_test_pass_mark_pct": 91,
        "fatality_rate_per_100k": 13,
        "source": "TOI editorial (WHO figure cited)",
    },
    "singapore": {
        "fatality_rate_per_100k": 1.4,
        "note": "Not the toughest licence test, yet the safest roads",
        "source": "TOI editorial (WHO figure cited)",
    },
}

ENFORCEMENT_GAP = {
    "unpaid_echallans_value_inr_crore": 23000,
    "reported_to": "Supreme Court (early this month, per article)",
    "example": "A Delhi-registered BMW with 42 challans for driving without PUCC",
    "proposed_licence_test_pass_mark": {"current_pct": 60, "proposed_pct": 75},
    "article_thesis": "Stricter tests alone will not make roads safe; "
                      "attitude change and strict enforcement are needed.",
    "source": "TOI editorial 'Sense & Licence'",
}

# Motor Vehicles (Amendment) Act 2019 - VERIFY before submitting
TRAFFIC_LAWS = {
    "helmet": "Riding without a helmet: fine of Rs 1,000 and possible 3-month licence disqualification (MV Act s.129 / 194D).",
    "seatbelt": "Driving without seatbelt: fine of Rs 1,000 (s.194B).",
    "drunk_driving": "Drunk driving: up to Rs 10,000 fine and/or up to 6 months jail for first offence (s.185).",
    "speeding": "Over-speeding: Rs 1,000-2,000 for light vehicles (s.183).",
    "no_licence": "Driving without a valid licence: Rs 5,000 (s.181).",
    "no_insurance": "Driving without insurance: Rs 2,000 (s.196).",
    "juvenile": "Offence by a juvenile: guardian/owner deemed guilty, Rs 25,000 fine and 3 years jail (s.199A).",
}

# Candidate policies. 'evidence' is a starting point; the LLM must justify further.
POLICY_OPTIONS = {
    "echallan_recovery": {
        "name": "E-challan recovery mechanism",
        "idea": "Link unpaid challans to licence renewal, vehicle registration, insurance renewal and fitness certificates; use Lok Adalats for settlement.",
        "evidence": "Article: Rs 23,000 cr unpaid across states shows weak deterrence from fines that are not collected.",
        "tradeoffs": "Hardship for poor drivers, risk of wrong challans being enforced, needs state-central data integration.",
    },
    "repeat_offender_suspension": {
        "name": "Repeat-offender licence suspension (points system)",
        "idea": "Demerit points per violation; automatic suspension at a threshold; mandatory retraining before reinstatement.",
        "evidence": "Article: a vehicle with 42 challans shows impunity for repeat offenders. Points systems are used in many countries (general knowledge, not from the article, verify before use).",
        "tradeoffs": "Livelihood impact on professional drivers, appeals backlog, risk of driving unlicensed.",
    },
    "enforcement_technology": {
        "name": "Automated enforcement technology",
        "idea": "Speed/red-light cameras, ANPR, body cams, integrated with e-challan so penalties are certain and quick.",
        "evidence": "General deterrence research (not from the article, verify before use): certainty and speed of penalty tend to matter more than severity. Article: Singapore has the safest roads (1.4 per lakh) without having the toughest licence test.",
        "tradeoffs": "High capital cost, privacy concerns, camera placement bias, maintenance, plate-spoofing.",
    },
    "awareness_campaigns": {
        "name": "Awareness and attitude-change campaigns",
        "idea": "School curriculum, mass media, workplace programmes for commercial drivers, tied to enforcement drives.",
        "evidence": "Article: attitudes will not change without enforcement. Campaigns as a complement to enforcement is general knowledge, verify before use.",
        "tradeoffs": "Hard to measure impact, slow, weak when not backed by enforcement.",
    },
    "licensing_reform": {
        "name": "Licensing test reform (practical + quality)",
        "idea": "Shift from pass-mark increases to practical skills testing and examiner audits.",
        "evidence": "Article: Vietnam has a 91% pass mark but a rate of 13 per lakh, so a harder test alone does not fix outcomes.",
        "tradeoffs": "Needs trained examiners and test tracks, corruption risk, possible access delays for applicants.",
    },
}
