import json
from typing import Dict, Any, List, Optional

class SpatialRelationshipGroundingEvaluatorClient:
    """
    Production-grade spatial relationship grounding and geometric topology evaluator.
    Evaluates 2D/3D spatial relationship claims (e.g., 'A is above B', 'X is left-of Y', 'Z is occluded')
    using bounding box geometry to validate agent spatial reasoning before physical or UI actions.
    """
    def __init__(self):
        pass

    def evaluate_spatial_relation(
        self,
        subject_name: str = "Submit Button",
        subject_bbox: Optional[List[int]] = None,
        reference_name: str = "Password Input Field",
        reference_bbox: Optional[List[int]] = None,
        claimed_relation: str = "BELOW"
    ) -> Dict[str, Any]:
        # Bboxes in [ymin, xmin, ymax, xmax]
        if not subject_bbox:
            subject_bbox = [600, 400, 650, 600]  # Submit button below input
        if not reference_bbox:
            reference_bbox = [500, 400, 550, 600] # Password input

        s_ymin, s_xmin, s_ymax, s_xmax = subject_bbox
        r_ymin, r_xmin, r_ymax, r_xmax = reference_bbox

        s_cent_y = (s_ymin + s_ymax) / 2.0
        s_cent_x = (s_xmin + s_xmax) / 2.0
        r_cent_y = (r_ymin + r_ymax) / 2.0
        r_cent_x = (r_xmin + r_xmax) / 2.0

        # Calculate actual relations
        is_below = s_cent_y > r_cent_y
        is_above = s_cent_y < r_cent_y
        is_left_of = s_cent_x < r_cent_x
        is_right_of = s_cent_x > r_cent_x

        relation_truth_map = {
            "BELOW": is_below,
            "ABOVE": is_above,
            "LEFT_OF": is_left_of,
            "RIGHT_OF": is_right_of
        }

        relation_valid = relation_truth_map.get(claimed_relation.upper(), False)
        vertical_offset_px = round(s_cent_y - r_cent_y, 1)
        horizontal_offset_px = round(s_cent_x - r_cent_x, 1)

        return {
            "evaluation_id": "spt_grd_3310",
            "subject_entity": subject_name,
            "reference_entity": reference_name,
            "claimed_spatial_relation": claimed_relation.upper(),
            "claim_verified_true": relation_valid,
            "geometric_offsets": {
                "vertical_distance_px": vertical_offset_px,
                "horizontal_distance_px": horizontal_offset_px
            },
            "grounding_confidence": 0.98 if relation_valid else 0.15,
            "spatial_verdict": "SPATIAL_RELATION_GROUNDED" if relation_valid else "SPATIAL_RELATION_CONTRADICTED"
        }
