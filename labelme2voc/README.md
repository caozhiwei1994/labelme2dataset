
## Convert to VOC-format Dataset

```bash
# It generates:
#   - data_dataset_voc/JPEGImages
#   - data_dataset_voc/SegmentationClass
#   - data_dataset_voc/SegmentationClassVisualization

python labelme2voc.py --input_dir data_annotated --output_dir data_dataset_voc --labels labels.txt
