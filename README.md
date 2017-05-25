# print-proxy

### Install
- `pip install -r Requirements.txt` (make sure that this installs into the AGS version of python (x64))
- Update `secrets.py` with your server path and quad word.
- Publish `Toolbox.tbx/PrintProxy` as synchronous gp task.
    - Pass `{}` as `Web_Map_as_JSON` parameter.

### Usage
This service should behave exactly the same as an out-of-the-box `ExportWebMap` service with only one difference: it requires an additional parameter, `ExportWebMapService_URL`. This is the URL to the print service that you want to proxy to.

If you are using the [`PrintTask`](https://developers.arcgis.com/javascript/jsapi/printtask-amd.html) class in the ESRI JS API then you can pass this additional parameter using the `extraParameters` property on [`PrintParameters`](https://developers.arcgis.com/javascript/jsapi/printparameters-amd.html#extraparameters). For example:
```js
params.extraParameters = {
    'ExportWebMapService_URL': config.urls.exportWebMap
}
```

If you are using the [`Print`](https://developers.arcgis.com/javascript/3/jsapi/print-amd.html) widget, then you can set the undocumented parameter `extraParams`.

```js
this.printer = new Print({
    map: ...,
    url: config.urls.printProxy,
    templates: [...]
}, this.printDiv);

this.printer.extraParams = {
    'ExportWebMapService_URL': config.urls.exportWebMap // eslint-disable-line
};
```

### Tests
- set `OPEN_QUAD_WORD = 'test-quad-word-replaced'`
- `python -m unittest test`
