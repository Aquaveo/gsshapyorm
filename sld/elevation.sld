<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd">
  <NamedLayer>
    <Name>elevation</Name>
    <UserStyle>
      <Name>elevation</Name>
      <Title>Elevation Map Style</Title>
      <Abstract>Classic elevation color progression</Abstract>
      <FeatureTypeStyle>
        <Rule>
          <RasterSymbolizer>
            <Opacity>1.0</Opacity>
            <ColorMap>
              <ColorMapEntry color="${env('color_no_data','#E12300')}" quantity="${env('val_no_data',0)}" label="nodata" opacity="0"/>
              <ColorMapEntry color="${env('color0','#96D257')}" quantity="${env('val0',0.00001)}" label="0"/>
              <ColorMapEntry color="${env('color1','#278C39')}" quantity="${env('val1',2000)}" label="1" />
              <ColorMapEntry color="${env('color2','#2A7B45')}" quantity="${env('val2',2100)}" label="2" />
              <ColorMapEntry color="${env('color3','#829C41')}" quantity="${env('val3',2200)}" label="3" />
              <ColorMapEntry color="${env('color4','#DBB82E')}" quantity="${env('val4',2300)}" label="4" />
              <ColorMapEntry color="${env('color5','#AE4818')}" quantity="${env('val5',2400)}" label="5"/>
              <ColorMapEntry color="${env('color6','#842511')}" quantity="${env('val6',2500)}" label="6"/>
              <ColorMapEntry color="${env('color7','#61370F')}" quantity="${env('val7',2600)}" label="7"/>
              <ColorMapEntry color="${env('color8','#806346')}" quantity="${env('val8',2700)}" label="8" />
              <ColorMapEntry color="${env('color9','#C2C2C2')}" quantity="${env('val9',2800)}" label="9" />
              <ColorMapEntry color="${env('color10','#FFFFFF')}" quantity="${env('val10',2900)}" label="10" />
            </ColorMap>
          </RasterSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
