from kedro.pipeline import Pipeline, node
from .nodes import interpolate_missing_values

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=interpolate_missing_values,
            inputs=[
                "raw_temperature_sensor",
                "params:data_col"
            ],
            outputs="cleaned_temperature_sensor",
            name="interpolate_missing_values",
            tags='clean_data'
        )
    ])
