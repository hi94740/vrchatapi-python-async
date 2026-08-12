# FileAnalysisAvatarStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**animator_count** | **int** |  | 
**audio_source_count** | **int** |  | 
**blend_shape_count** | **int** |  | 
**bone_count** | **int** |  | 
**bounds** | **List[float]** |  | 
**camera_count** | **int** |  | [optional] 
**cloth_count** | **int** |  | 
**constraint_count** | **int** |  | 
**constraint_depth** | **int** |  | 
**contact_count** | **int** |  | 
**custom_expressions** | **bool** |  | 
**customize_animation_layers** | **bool** |  | 
**enable_eye_look** | **bool** |  | 
**light_count** | **int** |  | 
**line_renderer_count** | **int** |  | 
**lip_sync** | **int** |  | 
**material_count** | **int** |  | 
**material_slots_used** | **int** |  | 
**mesh_count** | **int** |  | 
**mesh_indices** | **int** |  | 
**mesh_particle_max_polygons** | **int** |  | 
**mesh_polygons** | **int** |  | 
**mesh_vertices** | **int** |  | 
**particle_collision_enabled** | **bool** |  | 
**particle_system_count** | **int** |  | 
**particle_trails_enabled** | **bool** |  | 
**phys_bone_collider_count** | **int** |  | 
**phys_bone_collision_check_count** | **int** |  | 
**phys_bone_component_count** | **int** |  | 
**phys_bone_transform_count** | **int** |  | 
**physics_colliders** | **int** |  | 
**physics_rigidbodies** | **int** |  | 
**skinned_mesh_count** | **int** |  | 
**skinned_mesh_indices** | **int** |  | 
**skinned_mesh_polygons** | **int** |  | 
**skinned_mesh_vertices** | **int** |  | 
**total_cloth_vertices** | **int** |  | 
**total_indices** | **int** |  | 
**total_max_particles** | **int** |  | 
**total_polygons** | **int** |  | 
**total_texture_usage** | **int** |  | 
**total_vertices** | **int** |  | 
**trail_renderer_count** | **int** |  | 
**write_defaults_used** | **bool** |  | 

## Example

```python
from vrchatapi.models.file_analysis_avatar_stats import FileAnalysisAvatarStats

# TODO update the JSON string below
json = "{}"
# create an instance of FileAnalysisAvatarStats from a JSON string
file_analysis_avatar_stats_instance = FileAnalysisAvatarStats.from_json(json)
# print the JSON string representation of the object
print(FileAnalysisAvatarStats.to_json())

# convert the object into a dict
file_analysis_avatar_stats_dict = file_analysis_avatar_stats_instance.to_dict()
# create an instance of FileAnalysisAvatarStats from a dict
file_analysis_avatar_stats_from_dict = FileAnalysisAvatarStats.from_dict(file_analysis_avatar_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


