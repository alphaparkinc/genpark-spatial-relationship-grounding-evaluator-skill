import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SpatialRelationshipGroundingEvaluatorClient

def main():
    client = SpatialRelationshipGroundingEvaluatorClient()
    res = client.evaluate_spatial_relation()
    print("=== Spatial Relationship Grounding Evaluator Output ===")
    print(f"Claim: '{res['subject_entity']}' is {res['claimed_spatial_relation']} '{res['reference_entity']}'")
    print(f"Verified True: {res['claim_verified_true']} (Confidence: {res['grounding_confidence']*100}%)")
    print(f"Offsets: vertical={res['geometric_offsets']['vertical_distance_px']}px, horizontal={res['geometric_offsets']['horizontal_distance_px']}px")
    print(f"Verdict: {res['spatial_verdict']}")

if __name__ == '__main__':
    main()
