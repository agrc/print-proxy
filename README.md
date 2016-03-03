# print-proxy

### Install
- `pip install -r Requirements.txt` (make sure that this installs into the AGS version of python (x64))
- Publish `Toolbox.tbx/PrintProxy` as synchronous gp task.
    - Pass `{}` as `Web_Map_as_JSON` parameter.

### Usage
This service should behave exactly the same as an out-of-the-box `ExportWebMap` service with only one difference: it request an additional parameter, `ExportWebMapService_URL`. This is the URL to the print service that you want to proxy to.

If you are using the [`PrintTask`](https://developers.arcgis.com/javascript/jsapi/printtask-amd.html) class in the ESRI JS API then you can pass this additional parameter using the `extraParameters` property on [`PrintParameters`](https://developers.arcgis.com/javascript/jsapi/printparameters-amd.html#extraparameters).

### Tests
`nosetests`
