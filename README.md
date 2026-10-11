# Medical AI Polyp Bounding Box Annotation

## Overview

This project demonstrates a medical image annotation workflow for colorectal polyp detection using colonoscopy images from the Kvasir-SEG dataset.

A sample of 100 colonoscopy images was selected and manually annotated using bounding boxes in Label Studio. Each bounding box was used to localize the visible colorectal polyp within the image.

---

## Dataset

The project uses the Kvasir-SEG dataset, which contains colonoscopy images with corresponding polyp segmentation masks and bounding-box information.

For this project, a sample of 100 images was selected from the original dataset.

### Dataset Summary

| Property | Value |
|---|---:|
| Total images annotated | 100 |
| Annotation type | Bounding Box |
| Medical modality | Colonoscopy |
| Target finding | Colorectal Polyp |
| Annotation tool | Label Studio |
| Annotation label | Polyp |

---

## Project Objective

The objective of this project was to demonstrate a complete medical image annotation workflow, including:

- Medical image dataset preparation
- Image selection and organization
- Bounding-box annotation
- Manual annotation in Label Studio
- Annotation export
- Medical AI dataset organization

---

## Annotation Workflow

### 1. Dataset Preparation

A sample of 100 images was selected from the Kvasir-SEG dataset.

The images were organized into a dedicated project directory and prepared for annotation.

The selection process was automated using the `select_sample.py` script.

### 2. Label Studio Configuration

A Label Studio project named `Colonoscopy Polyp Bounding Box` was created.

The annotation interface was configured for object detection using rectangular bounding boxes.

The following label was used:

- `Polyp`

### 3. Manual Annotation

All 100 images were manually annotated in Label Studio.

For each image, a bounding box was drawn around the visible colorectal polyp.

The completed annotations were exported in JSON format for documentation and further use.

---

## Project Structure

```text
Medical_AI_Polyp_Bounding_Box/
│
├── images/
│   └── Original Kvasir-SEG images
│
├── masks/
│   └── Kvasir-SEG reference segmentation masks
│
├── sample_images/
│   └── 100 selected images used for annotation
│
├── kavsir_bboxes.json
│   └── Kvasir-SEG reference bounding-box information
│
├── select_sample.py
│   └── Script used to select the 100-image sample
│
├── project-10-at-2026-09-30-17-52-8e632aa2.json
│   └── Label Studio annotation export
│
└── README.md
