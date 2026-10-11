# Medical AI: Polyp Bounding Box Annotation

## Project Overview

This project demonstrates a medical image annotation workflow for colorectal polyp detection using endoscopic images from the Kvasir-SEG dataset.

Using Label Studio, I manually annotated 100 images with bounding boxes to identify polyps. The project focuses on image annotation, dataset organization, and preparation of labeled data for medical computer vision tasks.

## Project Details

- **Task:** Polyp detection and localization
- **Annotation tool:** Label Studio
- **Annotation type:** Bounding boxes
- **Target class:** Polyp
- **Number of annotated tasks:** 100
- **Image domain:** Gastrointestinal endoscopy

## Methodology

1. Selected endoscopic images for annotation.
2. Reviewed each image in Label Studio.
3. Manually drew bounding boxes around visible polyps.
4. Assigned the `Polyp` label.
5. Exported the annotations in JSON format for further analysis and potential use in machine learning workflows.

## Annotation Format

The Label Studio export contains the annotation coordinates, bounding box dimensions, image dimensions, and class labels.

The annotations are provided in:

`project-10-at-2026-09-30-17-52-8e632aa2.json`

## Skills Demonstrated

- Medical image annotation
- Bounding box labeling
- Label Studio
- Dataset preparation
- JSON annotation handling
- Medical computer vision workflows

## Dataset Acknowledgment

The project uses endoscopic images from the Kvasir-SEG dataset. The manual bounding box annotations were created as part of this project.

## Disclaimer

This is an educational portfolio project and is not intended for clinical diagnosis or direct clinical decision-making.
