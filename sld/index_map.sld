<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd">
  <NamedLayer>
    <Name>index</Name>
    <UserStyle>
      <Name>index</Name>
      <Title>Generic Index Map Style</Title>
      <Abstract>Discreet colors</Abstract>
      <FeatureTypeStyle>
        <Rule>
          <RasterSymbolizer>
            <ColorMap type="values">
              <ColorMapEntry color="${env('color_no_data','#E12300')}" quantity="${env('val_no_data',0)}" label="nodata" opacity="0"/>
              <ColorMapEntry color="${env('color1','#E12300')}" quantity="${env('val1',1)}" label="1"/>
              <ColorMapEntry color="${env('color2','#D38306')}" quantity="${env('val2',2)}" label="2"/>
              <ColorMapEntry color="${env('color3','#F4ED01')}" quantity="${env('val3',3)}" label="3"/>
              <ColorMapEntry color="${env('color4','#649C31')}" quantity="${env('val4',4)}" label="4"/>
              <ColorMapEntry color="${env('color5','#038DBB')}" quantity="${env('val5',5)}" label="5"/>
              <ColorMapEntry color="${env('color6','#0057D5')}" quantity="${env('val6',6)}" label="6"/>
              <ColorMapEntry color="${env('color7','#391B95')}" quantity="${env('val7',7)}" label="7"/>
              <ColorMapEntry color="${env('color8','#77239D')}" quantity="${env('val8',8)}" label="8"/>
              <ColorMapEntry color="${env('color9','#FE634D')}" quantity="${env('val9',9)}" label="9"/>
              <ColorMapEntry color="${env('color10','#FFB23C')}" quantity="${env('val10',10)}" label="10"/>
              <ColorMapEntry color="${env('color11','#FBF968')}" quantity="${env('val11',11)}" label="11"/>
              <ColorMapEntry color="${env('color12','#97D45F')}" quantity="${env('val12',12)}" label="12"/>
              <ColorMapEntry color="${env('color13','#00C7FF')}" quantity="${env('val13',13)}" label="13"/>
              <ColorMapEntry color="${env('color14','#3689FF')}" quantity="${env('val14',14)}" label="14"/>
              <ColorMapEntry color="${env('color15','#5A32EB')}" quantity="${env('val15',15)}" label="15"/>
              <ColorMapEntry color="${env('color16','#BC37F2')}" quantity="${env('val16',16)}" label="16"/>
              <ColorMapEntry color="${env('color17','#FCB5AF')}" quantity="${env('val17',17)}" label="17"/>
              <ColorMapEntry color="${env('color18','#FFD8A8')}" quantity="${env('val18',18)}" label="18"/>
              <ColorMapEntry color="${env('color19','#FFFCB5')}" quantity="${env('val19',19)}" label="19"/>
              <ColorMapEntry color="${env('color20','#CDE9B8')}" quantity="${env('val20',20)}" label="20"/>
              <ColorMapEntry color="${env('color21','#90E4FE')}" quantity="${env('val21',21)}" label="21"/>
              <ColorMapEntry color="${env('color22','#AAC4FD')}" quantity="${env('val22',22)}" label="22"/>
              <ColorMapEntry color="${env('color23','#B28CFB')}" quantity="${env('val23',23)}" label="23"/>
              <ColorMapEntry color="${env('color24','#E395FB')}" quantity="${env('val24',24)}" label="24"/>
              <ColorMapEntry color="${env('color25','#FE4310')}" quantity="${env('val25',25)}" label="25"/>
              <ColorMapEntry color="${env('color26','#FFAA00')}" quantity="${env('val26',26)}" label="26"/>
              <ColorMapEntry color="${env('color27','#FDFB44')}" quantity="${env('val27',27)}" label="27"/>
              <ColorMapEntry color="${env('color28','#75BA43')}" quantity="${env('val28',28)}" label="28"/>
              <ColorMapEntry color="${env('color29','#00A2D8')}" quantity="${env('val29',29)}" label="29"/>
              <ColorMapEntry color="${env('color30','#0460FF')}" quantity="${env('val30',30)}" label="30"/>
              <ColorMapEntry color="${env('color31','#4A24B7')}" quantity="${env('val31',31)}" label="31"/>
              <ColorMapEntry color="${env('color32','#9A2ABA')}" quantity="${env('val32',32)}" label="32"/>
              <ColorMapEntry color="${env('color33','#B51902')}" quantity="${env('val33',33)}" label="33"/>
              <ColorMapEntry color="${env('color34','#AB6702')}" quantity="${env('val34',34)}" label="34"/>
              <ColorMapEntry color="${env('color35','#C2BD00')}" quantity="${env('val35',35)}" label="35"/>
              <ColorMapEntry color="${env('color36','#4C7C28')}" quantity="${env('val36',36)}" label="36"/>
              <ColorMapEntry color="${env('color37','#00728B')}" quantity="${env('val37',37)}" label="37"/>
              <ColorMapEntry color="${env('color38','#0142A6')}" quantity="${env('val38',38)}" label="38"/>
              <ColorMapEntry color="${env('color39','#2C1378')}" quantity="${env('val39',39)}" label="39"/>
              <ColorMapEntry color="${env('color40','#63167E')}" quantity="${env('val40',40)}" label="40"/>
              <ColorMapEntry color="${env('color41','#FF8C85')}" quantity="${env('val41',41)}" label="41"/>
              <ColorMapEntry color="${env('color42','#FFC878')}" quantity="${env('val42',42)}" label="42"/>
              <ColorMapEntry color="${env('color43','#FDFA91')}" quantity="${env('val43',43)}" label="43"/>
              <ColorMapEntry color="${env('color44','#B0DC87')}" quantity="${env('val44',44)}" label="44"/>
              <ColorMapEntry color="${env('color45','#55D6FE')}" quantity="${env('val45',45)}" label="45"/>
              <ColorMapEntry color="${env('color46','#75A7FE')}" quantity="${env('val46',46)}" label="46"/>
              <ColorMapEntry color="${env('color47','#854FFB')}" quantity="${env('val47',47)}" label="47"/>
              <ColorMapEntry color="${env('color48','#D456FF')}" quantity="${env('val48',48)}" label="48"/>
              <ColorMapEntry color="${env('color49','#FFD8D9')}" quantity="${env('val49',49)}" label="49"/>
              <ColorMapEntry color="${env('color50','#FFEBD3')}" quantity="${env('val50',50)}" label="50"/>
              <ColorMapEntry color="${env('color51','#FFFCDB')}" quantity="${env('val51',51)}" label="51"/>
              <ColorMapEntry color="${env('color52','#E2EBDA')}" quantity="${env('val52',52)}" label="52"/>
              <ColorMapEntry color="${env('color53','#CAF2FE')}" quantity="${env('val53',53)}" label="53"/>
              <ColorMapEntry color="${env('color54','#D4E4FB')}" quantity="${env('val54',54)}" label="54"/>
              <ColorMapEntry color="${env('color55','#DACAFB')}" quantity="${env('val55',55)}" label="55"/>
              <ColorMapEntry color="${env('color56','#F1C9FE')}" quantity="${env('val56',56)}" label="56"/>
              <ColorMapEntry color="${env('color57','#830D00')}" quantity="${env('val57',57)}" label="57"/>
              <ColorMapEntry color="${env('color58','#794803')}" quantity="${env('val58',58)}" label="58"/>
              <ColorMapEntry color="${env('color59','#888901')}" quantity="${env('val59',59)}" label="59"/>
              <ColorMapEntry color="${env('color60','#3B571C')}" quantity="${env('val60',60)}" label="60"/>
              <ColorMapEntry color="${env('color61','#004B63')}" quantity="${env('val61',61)}" label="61"/>
              <ColorMapEntry color="${env('color62','#013078')}" quantity="${env('val62',62)}" label="62"/>
              <ColorMapEntry color="${env('color63','#180B51')}" quantity="${env('val63',63)}" label="63"/>
              <ColorMapEntry color="${env('color64','#450F5D')}" quantity="${env('val64',64)}" label="64"/>
              <ColorMapEntry color="${env('color65','#FF0000')}" quantity="${env('val65',65)}" label="65"/>
              <ColorMapEntry color="${env('color66','#FF8000')}" quantity="${env('val66',66)}" label="66"/>
              <ColorMapEntry color="${env('color67','#FFFF00')}" quantity="${env('val67',67)}" label="67"/>
              <ColorMapEntry color="${env('color68','#00FF00')}" quantity="${env('val68',68)}" label="68"/>
              <ColorMapEntry color="${env('color69','#00FFFF')}" quantity="${env('val69',69)}" label="69"/>
              <ColorMapEntry color="${env('color70','#0000FF')}" quantity="${env('val70',70)}" label="70"/>
              <ColorMapEntry color="${env('color71','#8000FF')}" quantity="${env('val71',71)}" label="71"/>
              <ColorMapEntry color="${env('color72','#800000')}" quantity="${env('val72',72)}" label="72"/>
              <ColorMapEntry color="${env('color73','#804000')}" quantity="${env('val73',73)}" label="73"/>
              <ColorMapEntry color="${env('color74','#808000')}" quantity="${env('val74',74)}" label="74"/>
              <ColorMapEntry color="${env('color75','#008000')}" quantity="${env('val75',75)}" label="75"/>
              <ColorMapEntry color="${env('color76','#008080')}" quantity="${env('val76',76)}" label="76"/>
              <ColorMapEntry color="${env('color77','#000080')}" quantity="${env('val77',77)}" label="77"/>
              <ColorMapEntry color="${env('color78','#400080')}" quantity="${env('val78',78)}" label="78"/>
              <ColorMapEntry color="${env('color79','#FF2A00')}" quantity="${env('val79',79)}" label="79"/>
              <ColorMapEntry color="${env('color80','#FFAA00')}" quantity="${env('val80',80)}" label="80"/>
              <ColorMapEntry color="${env('color81','#AAFF00')}" quantity="${env('val81',81)}" label="81"/>
              <ColorMapEntry color="${env('color82','#00FF55')}" quantity="${env('val82',82)}" label="82"/>
              <ColorMapEntry color="${env('color83','#00AAFF')}" quantity="${env('val83',83)}" label="83"/>
              <ColorMapEntry color="${env('color84','#2A00FF')}" quantity="${env('val84',84)}" label="84"/>
              <ColorMapEntry color="${env('color85','#8000AA')}" quantity="${env('val85',85)}" label="85"/>
              <ColorMapEntry color="${env('color86','#801500')}" quantity="${env('val86',86)}" label="86"/>
              <ColorMapEntry color="${env('color87','#805500')}" quantity="${env('val87',87)}" label="87"/>
              <ColorMapEntry color="${env('color88','#558000')}" quantity="${env('val88',88)}" label="88"/>
              <ColorMapEntry color="${env('color89','#00802A')}" quantity="${env('val89',89)}" label="89"/>
              <ColorMapEntry color="${env('color90','#005580')}" quantity="${env('val90',90)}" label="90"/>
              <ColorMapEntry color="${env('color91','#150080')}" quantity="${env('val91',91)}" label="91"/>
              <ColorMapEntry color="${env('color92','#FF5500')}" quantity="${env('val92',92)}" label="92"/>
              <ColorMapEntry color="${env('color93','#FFD400')}" quantity="${env('val93',93)}" label="93"/>
              <ColorMapEntry color="${env('color94','#55FF00')}" quantity="${env('val94',94)}" label="94"/>
              <ColorMapEntry color="${env('color95','#00FFAA')}" quantity="${env('val95',95)}" label="95"/>
              <ColorMapEntry color="${env('color96','#0055FF')}" quantity="${env('val96',96)}" label="96"/>
              <ColorMapEntry color="${env('color97','#5500FF')}" quantity="${env('val97',97)}" label="97"/>
              <ColorMapEntry color="${env('color98','#800055')}" quantity="${env('val98',98)}" label="98"/>
              <ColorMapEntry color="${env('color99','#802A00')}" quantity="${env('val99',99)}" label="99"/>
              <ColorMapEntry color="${env('color100','#806A00')}" quantity="${env('val100',100)}" label="100"/>
              <ColorMapEntry color="${env('color101','#2A8000')}" quantity="${env('val101',101)}" label="101"/>
              <ColorMapEntry color="${env('color102','#008055')}" quantity="${env('val102',102)}" label="102"/>
              <ColorMapEntry color="${env('color103','#002A80')}" quantity="${env('val103',103)}" label="103"/>
              <ColorMapEntry color="${env('color104','#2A0080')}" quantity="${env('val104',104)}" label="104"/>
            </ColorMap>
          </RasterSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
