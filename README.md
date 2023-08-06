# GeoSAM-Image-Encoder

This package is part of [Geo-SAM](https://github.com/coolzhao/Geo-SAM) and is used to encode image data into features recognized by Geo-SAM.

## Installation

It is recommended to use the latest version of pip to install **GeoSAM-Image-Encoder**.

``` BASH
pip install GeoSAM-Image-Encoder
```


## Usage

You can call this script in Python or Terminal.

### Using Python

```python
from geosam import encode_image

image_path = "path_to_image_file"
checkpoint_path = "path_to_checkpoint"
feature_dir = "output_feature_dir"

encode_image(image_path, checkpoint_path, feature_dir)
```

**Parameters:**

```
image_path: str or Path
    Path to the input image.
checkpoint_path: str or Path
    Path to the SAM checkpoint.
feature_dir: str or Path
    Path to the output feature directory.
model_type: one of ["vit_h", "vit_l", "vit_b"] or [0, 1, 2] or None, optional
    The type of the SAM model. If None, the model type will be 
    inferred from the checkpoint path. Default: None. 
bands: list of int, optional
    The bands to be used for encoding. Should not be more than three bands.
    If None, the first three bands (if available) will be used. Default: None.
stride: int, optional
    The stride of the sliding window. Default: 512.
extent: str, optional
    The extent of the image to be encoded. Should be in the format of
    "minx, miny, maxx, maxy, [crs]". If None, the extent of the input
    image will be used. Default: None.
value_range: tuple of float, optional
    The value range of the input image. If None, the value range will be
    automatically calculated from the input image. Default: None.
resolution: float, optional
    The resolution of the output feature in the unit of raster crs.
    If None, the resolution of the input image will be used. Default: None.
batch_size: int, optional
    The batch size for encoding. Default: 1.
gpu: bool, optional
    Whether to use GPU for encoding if available. Default: True.
gpu_id: int, optional
    The device id of the GPU to be used. Default: 0.
```


or using `setting.json` file

```python
from geosam import encode_image_from_cmd

setting_path = "path_to_setting_file.json"
feature_dir = "output_feature_dir"

cmd = f"image_encoder.py -s {setting_path} -f {feature_dir}"
encode_image_from_cmd(cmd.split())
```


### Using Terminal

Before running this script in terminal, you need to add the folder contains the image_encoder.py script to the environment variables. You can use the following code to view the absolute path of this folder.

```python
import geosam
print(geosam.folder)
```

Once the environment variables are configured, you can directly call this script in terminal.

```bash
image_encoder.py -s path_to_setting_file.json -f output_feature_dir
```

You can find all Parameters by running:

```bash
image_encoder.py -h
# or
image_encoder.py --help
```
