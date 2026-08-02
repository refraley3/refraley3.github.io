---
layout: default
title: Photo Stacking in Photoshop
description: A practical workflow for combining multiple photographs with different focal lengths or focus distances into a single composite image.
---

Combining multiple photographs can produce a result that is not possible with a single exposure. Whether extending depth of field through focus stacking or blending images taken at different focal lengths, Photoshop provides the tools to align and merge the photographs while preserving the sharpest and most useful portions of each frame.

The workflow below emphasizes non-destructive editing so adjustments can be revisited later.

---

## Before You Begin

For the best results:

- Photograph from a sturdy tripod.
- Disable image stabilization when mounted on a tripod.
- Use Manual Exposure so brightness remains constant.
- Use Manual White Balance.
- Avoid moving the camera between exposures.
- If changing focal lengths, keep the subject centered whenever possible.
- Photograph in RAW format whenever practical.

---

## 1. Prepare the Images

Process each RAW file using identical settings in Adobe Camera Raw or Lightroom.

Synchronize:

- White Balance
- Exposure
- Contrast
- Highlights and Shadows
- Lens Corrections
- Noise Reduction
- Sharpening

Open all images as layers in Photoshop.

**File → Scripts → Load Files into Stack**

Check:

- **Attempt to Automatically Align Source Images**

---

## 2. Align the Layers

Even with a tripod, slight movement usually occurs.

Select every image layer.

**Edit → Auto-Align Layers**

Choose:

- **Auto**

Photoshop will compensate for slight movement, scale changes, and perspective differences.

---

## 3. Arrange the Layers

A useful organization is:

- Widest focal length on the bottom
- Progressively longer focal lengths above

Rename the layers to identify the focal length or purpose.

Example:

- 100 mm
- 200 mm
- 400 mm

---

## 4. Add Layer Masks

Beginning with the top layer:

- Select the layer.
- Click **Add Layer Mask**.

Initially the mask should be white, revealing the entire layer.

---

## 5. Reveal Only the Best Portions

Select the layer mask.

Using a soft brush:

- Black conceals
- White reveals

Paint only the areas that benefit from the longer focal length or sharper focus.

Typical uses include:

- Sharper eyes on wildlife
- Better feather detail
- Cleaner flower petals
- Additional reach on the primary subject
- Improved background from another exposure

Use a low brush opacity (20–40%) when making gradual transitions.

---

## 6. Refine the Blend

Zoom to 100%.

Look for:

- Halos
- Double edges
- Misalignment
- Brightness changes
- Color shifts

Switch between black and white while painting on the mask until the transition appears natural.

---

## 7. Match Color and Tone

If one layer differs slightly:

Create a clipped Adjustment Layer.

Common adjustments:

- Curves
- Levels
- Color Balance
- Hue/Saturation

Adjust only the selected layer without affecting the entire composite.

---

## 8. Crop the Image

Auto-Alignment often leaves transparent edges.

Use the Crop Tool to remove empty areas.

---

## 9. Final Cleanup

Inspect the image at:

- 100%
- 200%

Correct any remaining distractions using:

- Clone Stamp
- Healing Brush
- Remove Tool

---

## 10. Save the Working File

Save the layered version first.

**File → Save As**

- Photoshop (*.PSD)

Then export a finished copy.

**File → Export → Export As**

or

**File → Save a Copy**

- JPEG
- TIFF

---

## Notes on Different Focal Lengths

Blending different focal lengths differs from traditional focus stacking.

Changing focal length alters:

- Magnification
- Perspective (slightly)
- Subject size
- Depth of field

Photoshop's **Auto-Align Layers** usually compensates for modest differences, but very large focal length changes may require manual resizing or slight transformations.

The technique works best when:

- The camera remains stationary.
- The focal length changes are moderate.
- The primary subject occupies approximately the same location in each frame.

Rather than attempting to merge entire images, blend only the portions that benefit from each focal length.

---

## Common Applications

- Wildlife portraits with additional feather or fur detail.
- Flower photography combining different focus distances.
- Macro photography with increased depth of field.
- Combining a wider environmental view with a closer portrait of the subject.
- Replacing a distracting background with one from another exposure.
- Recovering detail from a sequence of nearly identical photographs.

---

## Tips

- Keep every layer until editing is complete.
- Name layers with focal length or focus distance.
- Use layer masks instead of erasing pixels.
- Frequently toggle layer visibility to verify the blend.
- Save incremental PSD versions during complex composites.
- Work slowly around fine details such as hair, feathers, and insect antennae.