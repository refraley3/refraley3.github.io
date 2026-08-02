---
layout: default
title: Printing Photographs with Adobe Photoshop
description: A color-managed Photoshop workflow for preparing photographic prints, including soft proofing, print-brightness adjustments, output sharpening, and printer settings.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A practical workflow for preparing photographic prints in Adobe Photoshop, developed while testing print adjustments for **Morning Stillness** and **Storm Light**.
{:.caption}

Physical prints frequently appear darker than the same photograph displayed on a monitor. This workflow uses a separate Photoshop print file, an appropriate printer-and-paper color profile, and a print-specific midtone adjustment to compensate for the difference between an illuminated screen and reflective paper.

## 1. Export Camera Raw to JPEG

Open the original RAW file in Adobe Camera Raw and complete the normal photographic adjustments.

Export a full-resolution JPEG using the following settings:

| Setting           | Value               |
| ----------------- | ------------------- |
| Quality           | Maximum             |
| Color Space       | Adobe RGB (1998)    |
| Image Sizing      | Do not resize       |
| Resolution        | 300 pixels per inch |
| Output Sharpening | None                |

Save the JPEG in a dedicated subfolder, such as:

`Print`

The subfolder keeps the working print copy separate from the original image, website files, and other exported versions.

The full-resolution JPEG becomes the source image for the Photoshop print file.

## 2. Open the JPEG in Photoshop

Open the exported JPEG in Adobe Photoshop.

Immediately save a working copy:

**File → Save As → Photoshop (.PSD)**

Saving the image as a PSD preserves adjustment layers and prevents the exported JPEG from being overwritten.

## 3. Confirm the Canvas and Print Size

Before resizing the photograph, establish the physical boundaries of the finished print.

### Establish the Canvas or Trim Boundary

Draw a rectangle to represent the outer canvas or trim boundary.

The Canvas Size may be determined by:

* The inside dimensions of the frame
* The final trimmed size of the print
* The available photo-paper size
* The printer's maximum printable area

The photo paper may be larger than the frame or finished print and may need to be trimmed after printing. The paper size and Canvas Size may also be limited by the printer.

For the current printer, the practical maximum paper size is approximately **17 × 11 inches**. A larger-format printer may allow the Canvas Size to be based primarily on the frame, matboard, or intended finished dimensions.

To set the document canvas to the required dimensions, select:

**Image → Canvas Size**

Enter the intended width and height of the paper or finished trimmed print.

Confirm the anchor position before applying the change. A centered anchor adds or removes canvas evenly around the photograph.

Modify the Canvas Size to fit the outer boundary rectangle. The boundary rectangle may be retained as a temporary Shape layer or replaced with guides after the canvas dimensions have been established.

Using Canvas Size for the outside boundary preserves space for positioning, mounting, and trimming without changing the dimensions or resolution of the photograph itself.

### Establish the Matboard Opening

Draw a second rectangle to represent the visible opening in the matboard.

Position the matboard-opening rectangle within the canvas or trim-boundary rectangle.

Account for:

* The width of the matboard
* The placement of the opening within the frame
* Any intentionally wider lower mat margin
* The amount of photograph concealed beneath the matboard
* The space required for trimming and mounting

The matboard opening should normally overlap the edges of the photograph slightly so no unprinted paper is visible after assembly.

### Resize the Photograph

Select the photograph and determine the image size needed to fill the matboard opening.

Select:

**Image → Image Size**

Enter the intended physical print dimensions.

For a 30 × 20-inch photograph:

| Setting  | Value     |
| -------- | --------- |
| Width    | 30 inches |
| Height   | 20 inches |
| Resample | Off       |

A full-resolution Canon EOS 5D Mark IV image measuring approximately 6720 × 4480 pixels produces about 224 pixels per inch at 30 × 20 inches. This is adequate for a wall print viewed from a normal distance.

Do not enlarge or resample the image unless the printer or print service specifically requires it.

After confirming the image dimensions, use the Move or Free Transform controls to position the photograph beneath the matboard-opening rectangle:

**Edit → Free Transform**

Maintain the original aspect ratio while scaling. Make sure the image extends slightly beyond every edge of the matboard opening.

Adjust the size or position of the matboard opening as required to achieve the desired composition. Verify that important subject matter will not be concealed by the matboard.

## 4. Soft-Proof the Photograph

Select:

**View → Proof Setup → Custom**

Use the following settings:

| Setting                  | Value                                       |
| ------------------------ | ------------------------------------------- |
| Device to Simulate       | ICC profile for the exact printer and paper |
| Preserve RGB Numbers     | Off                                         |
| Rendering Intent         | Relative Colorimetric                       |
| Black Point Compensation | On                                          |
| Simulate Paper Color     | On for evaluation                           |
| Simulate Black Ink       | On                                          |

Enable **Preview** to compare the normal image with the simulated print.

The simulated paper may make the photograph appear slightly flatter and darker. This is expected. The soft proof helps identify where a print-specific adjustment may be necessary.

Toggle the soft proof on and off with:

**View → Proof Colors**

## 5. Add a Print-Brightness Adjustment

Create a Curves adjustment layer:

**Layer → New Adjustment Layer → Curves**

Name the layer:

`Print Brightness`

Raise the middle portion of the curve slightly while leaving the black point and highlights anchored.

The purpose is to brighten the middle tones without washing out the shadows or losing highlight detail.

For **Storm Light**, concentrate the adjustment on:

* The meadow
* The distant trees
* The lower storm clouds
* The faint rainbow

Preserve the deeper tones in the upper clouds so the photograph retains its storm-light atmosphere.

Use a gentle adjustment. The Photoshop print version may appear slightly brighter than the preferred screen version. This additional brightness helps compensate for the reflective nature of a physical print.

## 6. Apply Output Sharpening

Evaluate the photograph at 100% magnification.

Apply modest output sharpening only after establishing the final print dimensions.

Select:

**Filter → Sharpen → Smart Sharpen**

Sharpen enough to restore fine detail in areas such as:

* Grass and meadow texture
* Distant trees
* Cloud edges
* Fine foreground detail

Avoid obvious halos around high-contrast edges or excessive sharpening of image noise.

A print file may look slightly sharper on the monitor than the normal gallery version because some apparent sharpness is lost during printing.

## 7. Open the Photoshop Print Dialog

Select:

**File → Print**

Under **Color Management**, use the following settings:

| Setting                  | Value                                       |
| ------------------------ | ------------------------------------------- |
| Color Handling           | Photoshop Manages Colors                    |
| Printer Profile          | ICC profile for the exact printer and paper |
| Rendering Intent         | Relative Colorimetric                       |
| Black Point Compensation | On                                          |

Also confirm:

* The correct paper size
* The correct portrait or landscape orientation
* The correct print dimensions
* **Center Image** is enabled unless a custom position is required
* Scale is set to 100% when the document has already been prepared at the final size

## 8. Configure the Printer Driver

Open **Print Settings** and choose:

* The exact paper or media type
* High or maximum print quality
* The correct paper source
* Borderless printing only when required
* Printer color correction set to **Off**, **None**, or **No Color Adjustment**

When **Photoshop Manages Colors** is selected, the printer driver must not apply an additional color correction.

Allowing both Photoshop and the printer driver to manage color can produce inaccurate colors, excessive contrast, or an unexpectedly dark print.

## 9. Make a Test Print

Before producing a large print, make a smaller proof or test strip on the same paper.

The proof should include representative portions of the photograph:

* The darkest shadows
* Important middle tones
* Highlight detail
* Fine texture
* Subtle color transitions

For **Storm Light**, include:

* The darkest storm clouds
* The meadow
* The distant tree line
* The rainbow
* An area containing fine detail

Allow the print to dry before making a final evaluation. Some inks and papers change slightly as they dry.

Evaluate the proof under lighting similar to the location where the finished print will be displayed.

Pay particular attention to the middle tones. A print may retain both shadow and highlight detail while still appearing too dark overall.

## 10. Revise and Save the Print File

Adjust the `Print Brightness` Curves layer after evaluating the proof.

Keep the print correction in the separate Photoshop print file. Do not alter the original Camera Raw processing or the website version solely to compensate for the physical print.

Save the final PSD with:

* The adjustment layers intact
* The document color profile embedded
* The final print dimensions established
* The printer-and-paper combination documented in the filename or file notes

The saved PSD can be reused for replacement prints made with the same printer, paper, profile, and printer-driver settings.

## Important Printing Principles

### Use a Separate Print Version

The website image and the print image serve different purposes. A photograph optimized for an illuminated display may require brighter middle tones when printed on reflective paper.

### Use the Exact Printer-and-Paper Profile

An ICC profile is specific to the printer, ink, and paper combination. A profile intended for another paper may produce inaccurate colors and tonal values.

### Avoid Double Color Management

Choose one color-management method:

* Photoshop manages the colors, or
* The printer manages the colors

Do not enable both.

For a controlled photographic workflow, use **Photoshop Manages Colors** and disable color correction in the printer driver.

### Judge the Physical Proof

The monitor is a preparation tool, but the physical proof is the final reference. Evaluate the print under appropriate lighting and revise the print-specific adjustment layer when necessary.
