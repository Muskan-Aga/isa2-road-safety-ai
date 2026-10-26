# tools/registry.py
import json
from data import FATALITY_STATS, ENFORCEMENT_GAP, TRAFFIC_LAWS, POLICY_OPTIONS


def get_fatality_stats(country: str) -> dict:
    key = country.strip().lower()
    return FATALITY_STATS.get(key, {"error": f"No data for '{country}'. Available: {list(FATALITY_STATS)}"})


def get_enforcement_gap() -> dict:
    return ENFORCEMENT_GAP


def lookup_traffic_law(topic: str) -> dict:
    t = topic.strip().lower()
    matches = {k: v for k, v in TRAFFIC_LAWS.items() if k in t or t in k}
    return matches or {"available_topics": list(TRAFFIC_LAWS)}


def get_policy_options(focus: str = "all") -> dict:
    f = focus.strip().lower()
    if f == "all" or not f:
        return POLICY_OPTIONS
    matches = {k: v for k, v in POLICY_OPTIONS.items() if f in k or f in v["name"].lower()}
    return matches or POLICY_OPTIONS


TOOL_FUNCTIONS = {
    "get_fatality_stats": get_fatality_stats,
    "get_enforcement_gap": get_enforcement_gap,
    "lookup_traffic_law": lookup_traffic_law,
    "get_policy_options": get_policy_options,
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_fatality_stats",
            "description": "Get road fatality statistics for 'india', 'vietnam' or 'singapore'.",
            "parameters": {
                "type": "object",
                "properties": {"country": {"type": "string"}},
                "required": ["country"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_enforcement_gap",
            "description": "Get data on unpaid e-challans, repeat offenders and the proposed licence test change.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "lookup_traffic_law",
            "description": "Look up Motor Vehicles Act penalties by topic (helmet, seatbelt, drunk_driving, speeding, no_licence, no_insurance, juvenile).",
            "parameters": {
                "type": "object",
                "properties": {"topic": {"type": "string"}},
                "required": ["topic"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_policy_options",
            "description": "Get candidate policy options with idea, evidence and trade-offs. Use focus='all' for everything.",
            "parameters": {
                "type": "object",
                "properties": {"focus": {"type": "string"}},
            },
        },
    },
]


def run_tool(name: str, args: dict):
    fn = TOOL_FUNCTIONS.get(name)
    if fn is None:
        return {"error": f"Unknown tool {name}"}
    try:
        return fn(**args)
    except Exception as e:
        return {"error": str(e)}
