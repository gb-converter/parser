# SOAP (formerly an acronym for Simple Object Access Protocol) is a messaging protocol specification for exchanging
# structured information in the implementation of web services in computer networks.

from zeep import Client, AsyncClient
from datetime import date

client = Client('http://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?wsdl')
service12 = client.bind('DailyInfo', 'DailyInfoSoap12')

# Получение списка действующих валют
# print(service1.EnumValutes('false'))
# Получение "сегодняшнего" курса валют
# print(service12.GetCursOnDate(date.today()))
# print(service1.GetCursOnDateXML(date.today()))

# Bindings:
#      Soap11Binding: {http://web.cbr.ru/}DailyInfoSoap
#      Soap12Binding: {http://web.cbr.ru/}DailyInfoSoap12

# Service: DailyInfo
#      Port: DailyInfoSoap (Soap11Binding: {http://web.cbr.ru/}DailyInfoSoap)
#          Operations:
#             GetCursDynamic(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string) -> GetCursDynamicResult: {schema: , _value_1: ANY}
#             GetCursDynamicXML(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string) -> GetCursDynamicXMLResult: {_value_1: ANY}
#             GetCursOnDate(On_date: xsd:dateTime) -> GetCursOnDateResult: {schema: , _value_1: ANY}
#             GetCursOnDateXML(On_date: xsd:dateTime) -> GetCursOnDateXMLResult: {_value_1: ANY}

# (.venv) H:\PyCharmProjects\parser>python -m zeep http://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?WSDL
#
# Prefixes:
#      xsd: http://www.w3.org/2001/XMLSchema
#      ns0: http://web.cbr.ru/
#
# Global elements:
#      ns0:AllDataInfoXML()
#      ns0:AllDataInfoXMLResponse(AllDataInfoXMLResult: {_value_1: ANY})
#      ns0:Bauction(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:BauctionResponse(BauctionResult: {schema: , _value_1: ANY})
#      ns0:BauctionXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:BauctionXMLResponse(BauctionXMLResult: {_value_1: ANY})
#      ns0:BiCurBacket()
#      ns0:BiCurBacketResponse(BiCurBacketResult: {schema: , _value_1: ANY})
#      ns0:BiCurBacketXML()
#      ns0:BiCurBacketXMLResponse(BiCurBacketXMLResult: {_value_1: ANY})
#      ns0:BiCurBase(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:BiCurBaseResponse(BiCurBaseResult: {schema: , _value_1: ANY})
#      ns0:BiCurBaseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:BiCurBaseXMLResponse(BiCurBaseXMLResult: {_value_1: ANY})
#      ns0:Coins_base(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:Coins_baseResponse(Coins_baseResult: {schema: , _value_1: ANY})
#      ns0:Coins_baseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:Coins_baseXMLResponse(Coins_baseXMLResult: {_value_1: ANY})
#      ns0:DV(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:DVResponse(DVResult: {schema: , _value_1: ANY})
#      ns0:DVXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:DVXMLResponse(DVXMLResult: {_value_1: ANY})
#      ns0:DepoDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:DepoDynamicResponse(DepoDynamicResult: {schema: , _value_1: ANY})
#      ns0:DepoDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:DepoDynamicXMLResponse(DepoDynamicXMLResult: {_value_1: ANY})
#      ns0:DragMetDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:DragMetDynamicResponse(DragMetDynamicResult: {schema: , _value_1: ANY})
#      ns0:DragMetDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:DragMetDynamicXMLResponse(DragMetDynamicXMLResult: {_value_1: ANY})
#      ns0:EnumReutersValutes()
#      ns0:EnumReutersValutesResponse(EnumReutersValutesResult: {schema: , _value_1: ANY})
#      ns0:EnumReutersValutesXML()
#      ns0:EnumReutersValutesXMLResponse(EnumReutersValutesXMLResult: {_value_1: ANY})
#      ns0:EnumValutes(Seld: xsd:boolean)
#      ns0:EnumValutesResponse(EnumValutesResult: {schema: , _value_1: ANY})
#      ns0:EnumValutesXML(Seld: xsd:boolean)
#      ns0:EnumValutesXMLResponse(EnumValutesXMLResult: {_value_1: ANY})
#      ns0:FixingBase(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:FixingBaseResponse(FixingBaseResult: {schema: , _value_1: ANY})
#      ns0:FixingBaseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:FixingBaseXMLResponse(FixingBaseXMLResult: {_value_1: ANY})
#      ns0:GetCursDynamic(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string)
#      ns0:GetCursDynamicResponse(GetCursDynamicResult: {schema: , _value_1: ANY})
#      ns0:GetCursDynamicXML(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string)
#      ns0:GetCursDynamicXMLResponse(GetCursDynamicXMLResult: {_value_1: ANY})
#      ns0:GetCursOnDate(On_date: xsd:dateTime)
#      ns0:GetCursOnDateResponse(GetCursOnDateResult: {schema: , _value_1: ANY})
#      ns0:GetCursOnDateXML(On_date: xsd:dateTime)
#      ns0:GetCursOnDateXMLResponse(GetCursOnDateXMLResult: {_value_1: ANY})
#      ns0:GetLatestDate()
#      ns0:GetLatestDateResponse(GetLatestDateResult: xsd:string)
#      ns0:GetLatestDateSeld()
#      ns0:GetLatestDateSeldResponse(GetLatestDateSeldResult: xsd:string)
#      ns0:GetLatestDateTime()
#      ns0:GetLatestDateTimeResponse(GetLatestDateTimeResult: xsd:dateTime)
#      ns0:GetLatestDateTimeSeld()
#      ns0:GetLatestDateTimeSeldResponse(GetLatestDateTimeSeldResult: xsd:dateTime)
#      ns0:GetLatestReutersDateTime()
#      ns0:GetLatestReutersDateTimeResponse(GetLatestReutersDateTimeResult: xsd:dateTime)
#      ns0:GetReutersCursDynamic(FromDate: xsd:dateTime, ToDate: xsd:dateTime, NumCode: xsd:int)
#      ns0:GetReutersCursDynamicResponse(GetReutersCursDynamicResult: {schema: , _value_1: ANY})
#      ns0:GetReutersCursDynamicXML(FromDate: xsd:dateTime, ToDate: xsd:dateTime, NumCode: xsd:int)
#      ns0:GetReutersCursDynamicXMLResponse(GetReutersCursDynamicXMLResult: {_value_1: ANY})
#      ns0:GetReutersCursOnDate(On_date: xsd:dateTime)
#      ns0:GetReutersCursOnDateResponse(GetReutersCursOnDateResult: {schema: , _value_1: ANY})
#      ns0:GetReutersCursOnDateXML(On_date: xsd:dateTime)
#      ns0:GetReutersCursOnDateXMLResponse(GetReutersCursOnDateXMLResult: {_value_1: ANY})
#      ns0:GetSeldCursOnDate(On_date: xsd:dateTime)
#      ns0:GetSeldCursOnDateResponse(GetSeldCursOnDateResult: {schema: , _value_1: ANY})
#      ns0:GetSeldCursOnDateXML(On_date: xsd:dateTime)
#      ns0:GetSeldCursOnDateXMLResponse(GetSeldCursOnDateXMLResult: {_value_1: ANY})
#      ns0:KeyRate(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:KeyRateResponse(KeyRateResult: {schema: , _value_1: ANY})
#      ns0:KeyRateXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:KeyRateXMLResponse(KeyRateXMLResult: {_value_1: ANY})
#      ns0:MKR(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:MKRResponse(MKRResult: {schema: , _value_1: ANY})
#      ns0:MKRXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:MKRXMLResponse(MKRXMLResult: {_value_1: ANY})
#      ns0:MainInfoXML()
#      ns0:MainInfoXMLResponse(MainInfoXMLResult: {_value_1: ANY})
#      ns0:NewsInfo(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:NewsInfoResponse(NewsInfoResult: {schema: , _value_1: ANY})
#      ns0:NewsInfoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:NewsInfoXMLResponse(NewsInfoXMLResult: {_value_1: ANY})
#      ns0:OmodInfoXML()
#      ns0:OmodInfoXMLResponse(OmodInfoXMLResult: {_value_1: ANY})
#      ns0:OstatDepo(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:OstatDepoResponse(OstatDepoResult: {schema: , _value_1: ANY})
#      ns0:OstatDepoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:OstatDepoXMLResponse(OstatDepoXMLResult: {_value_1: ANY})
#      ns0:OstatDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:OstatDynamicResponse(OstatDynamicResult: {schema: , _value_1: ANY})
#      ns0:OstatDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:OstatDynamicXMLResponse(OstatDynamicXMLResult: {_value_1: ANY})
#      ns0:Overnight(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:OvernightResponse(OvernightResult: {schema: , _value_1: ANY})
#      ns0:OvernightXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:OvernightXMLResponse(OvernightXMLResult: {_value_1: ANY})
#      ns0:ROISfix(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:ROISfixResponse(ROISfixResult: {schema: , _value_1: ANY})
#      ns0:ROISfixXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:ROISfixXMLResponse(ROISfixXMLResult: {_value_1: ANY})
#      ns0:RepoDebtUSD(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:RepoDebtUSDResponse(RepoDebtUSDResult: {schema: , _value_1: ANY})
#      ns0:RepoDebtUSDXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:RepoDebtUSDXMLResponse(RepoDebtUSDXMLResult: {_value_1: ANY})
#      ns0:Repo_debt(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:Repo_debtResponse(Repo_debtResult: {schema: , _value_1: ANY})
#      ns0:Repo_debtXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:Repo_debtXMLResponse(Repo_debtXMLResult: {_value_1: ANY})
#      ns0:Ruonia(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:RuoniaResponse(RuoniaResult: {schema: , _value_1: ANY})
#      ns0:RuoniaXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:RuoniaXMLResponse(RuoniaXMLResult: {_value_1: ANY})
#      ns0:Saldo(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SaldoResponse(SaldoResult: {schema: , _value_1: ANY})
#      ns0:SaldoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SaldoXMLResponse(SaldoXMLResult: {_value_1: ANY})
#      ns0:SwapDayTotal(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapDayTotalResponse(SwapDayTotalResult: {schema: , _value_1: ANY})
#      ns0:SwapDayTotalXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapDayTotalXMLResponse(SwapDayTotalXMLResult: {_value_1: ANY})
#      ns0:SwapDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapDynamicResponse(SwapDynamicResult: {schema: , _value_1: ANY})
#      ns0:SwapDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapDynamicXMLResponse(SwapDynamicXMLResult: {_value_1: ANY})
#      ns0:SwapInfoSellUSD(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapInfoSellUSDResponse(SwapInfoSellUSDResult: {schema: , _value_1: ANY})
#      ns0:SwapInfoSellUSDVol(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapInfoSellUSDVolResponse(SwapInfoSellUSDVolResult: {schema: , _value_1: ANY})
#      ns0:SwapInfoSellUSDVolXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapInfoSellUSDVolXMLResponse(SwapInfoSellUSDVolXMLResult: {_value_1: ANY})
#      ns0:SwapInfoSellUSDXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapInfoSellUSDXMLResponse(SwapInfoSellUSDXMLResult: {_value_1: ANY})
#      ns0:SwapMonthTotal(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapMonthTotalResponse(SwapMonthTotalResult: {schema: , _value_1: ANY})
#      ns0:SwapMonthTotalXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:SwapMonthTotalXMLResponse(SwapMonthTotalXMLResult: {_value_1: ANY})
#      ns0:ValIntDay(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:ValIntDayResponse(ValIntDayResult: {schema: , _value_1: ANY})
#      ns0:ValIntDayXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:ValIntDayXMLResponse(ValIntDayXMLResult: {_value_1: ANY})
#      ns0:XVol(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:XVolResponse(XVolResult: {schema: , _value_1: ANY})
#      ns0:XVolXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:XVolXMLResponse(XVolXMLResult: {_value_1: ANY})
#      ns0:mrrf(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:mrrf7D(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:mrrf7DResponse(mrrf7DResult: {schema: , _value_1: ANY})
#      ns0:mrrf7DXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:mrrf7DXMLResponse(mrrf7DXMLResult: {_value_1: ANY})
#      ns0:mrrfResponse(mrrfResult: {schema: , _value_1: ANY})
#      ns0:mrrfXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime)
#      ns0:mrrfXMLResponse(mrrfXMLResult: {_value_1: ANY})
#
#
# Global types:
#      xsd:anyType
#      xsd:ENTITIES
#      xsd:ENTITY
#      xsd:ID
#      xsd:IDREF
#      xsd:IDREFS
#      xsd:NCName
#      xsd:NMTOKEN
#      xsd:NMTOKENS
#      xsd:NOTATION
#      xsd:Name
#      xsd:QName
#      xsd:anySimpleType
#      xsd:anyURI
#      xsd:base64Binary
#      xsd:boolean
#      xsd:byte
#      xsd:date
#      xsd:dateTime
#      xsd:decimal
#      xsd:double
#      xsd:duration
#      xsd:float
#      xsd:gDay
#      xsd:gMonth
#      xsd:gMonthDay
#      xsd:gYear
#      xsd:gYearMonth
#      xsd:hexBinary
#      xsd:int
#      xsd:integer
#      xsd:language
#      xsd:long
#      xsd:negativeInteger
#      xsd:nonNegativeInteger
#      xsd:nonPositiveInteger
#      xsd:normalizedString
#      xsd:positiveInteger
#      xsd:short
#      xsd:string
#      xsd:time
#      xsd:token
#      xsd:unsignedByte
#      xsd:unsignedInt
#      xsd:unsignedLong
#      xsd:unsignedShort
#
# Bindings:
#      Soap11Binding: {http://web.cbr.ru/}DailyInfoSoap
#      Soap12Binding: {http://web.cbr.ru/}DailyInfoSoap12
#
# Service: DailyInfo
#      Port: DailyInfoSoap (Soap11Binding: {http://web.cbr.ru/}DailyInfoSoap)
#          Operations:
#             AllDataInfoXML() -> AllDataInfoXMLResult: {_value_1: ANY}
#             Bauction(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BauctionResult: {schema: , _value_1: ANY}
#             BauctionXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BauctionXMLResult: {_value_1: ANY}
#             BiCurBacket() -> BiCurBacketResult: {schema: , _value_1: ANY}
#             BiCurBacketXML() -> BiCurBacketXMLResult: {_value_1: ANY}
#             BiCurBase(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BiCurBaseResult: {schema: , _value_1: ANY}
#             BiCurBaseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BiCurBaseXMLResult: {_value_1: ANY}
#             Coins_base(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Coins_baseResult: {schema: , _value_1: ANY}
#             Coins_baseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Coins_baseXMLResult: {_value_1: ANY}
#             DV(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DVResult: {schema: , _value_1: ANY}
#             DVXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DVXMLResult: {_value_1: ANY}
#             DepoDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DepoDynamicResult: {schema: , _value_1: ANY}
#             DepoDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DepoDynamicXMLResult: {_value_1: ANY}
#             DragMetDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DragMetDynamicResult: {schema: , _value_1: ANY}
#             DragMetDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DragMetDynamicXMLResult: {_value_1: ANY}
#             EnumReutersValutes() -> EnumReutersValutesResult: {schema: , _value_1: ANY}
#             EnumReutersValutesXML() -> EnumReutersValutesXMLResult: {_value_1: ANY}
#             EnumValutes(Seld: xsd:boolean) -> EnumValutesResult: {schema: , _value_1: ANY}
#             EnumValutesXML(Seld: xsd:boolean) -> EnumValutesXMLResult: {_value_1: ANY}
#             FixingBase(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> FixingBaseResult: {schema: , _value_1: ANY}
#             FixingBaseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> FixingBaseXMLResult: {_value_1: ANY}
#             GetCursDynamic(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string) -> GetCursDynamicResult: {schema: , _value_1: ANY}
#             GetCursDynamicXML(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string) -> GetCursDynamicXMLResult: {_value_1: ANY}
#             GetCursOnDate(On_date: xsd:dateTime) -> GetCursOnDateResult: {schema: , _value_1: ANY}
#             GetCursOnDateXML(On_date: xsd:dateTime) -> GetCursOnDateXMLResult: {_value_1: ANY}
#             GetLatestDate() -> GetLatestDateResult: xsd:string
#             GetLatestDateSeld() -> GetLatestDateSeldResult: xsd:string
#             GetLatestDateTime() -> GetLatestDateTimeResult: xsd:dateTime
#             GetLatestDateTimeSeld() -> GetLatestDateTimeSeldResult: xsd:dateTime
#             GetLatestReutersDateTime() -> GetLatestReutersDateTimeResult: xsd:dateTime
#             GetReutersCursDynamic(FromDate: xsd:dateTime, ToDate: xsd:dateTime, NumCode: xsd:int) -> GetReutersCursDynamicResult: {schema: , _value_1: ANY}
#             GetReutersCursDynamicXML(FromDate: xsd:dateTime, ToDate: xsd:dateTime, NumCode: xsd:int) -> GetReutersCursDynamicXMLResult: {_value_1: ANY}
#             GetReutersCursOnDate(On_date: xsd:dateTime) -> GetReutersCursOnDateResult: {schema: , _value_1: ANY}
#             GetReutersCursOnDateXML(On_date: xsd:dateTime) -> GetReutersCursOnDateXMLResult: {_value_1: ANY}
#             GetSeldCursOnDate(On_date: xsd:dateTime) -> GetSeldCursOnDateResult: {schema: , _value_1: ANY}
#             GetSeldCursOnDateXML(On_date: xsd:dateTime) -> GetSeldCursOnDateXMLResult: {_value_1: ANY}
#             KeyRate(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> KeyRateResult: {schema: , _value_1: ANY}
#             KeyRateXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> KeyRateXMLResult: {_value_1: ANY}
#             MKR(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> MKRResult: {schema: , _value_1: ANY}
#             MKRXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> MKRXMLResult: {_value_1: ANY}
#             MainInfoXML() -> MainInfoXMLResult: {_value_1: ANY}
#             NewsInfo(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> NewsInfoResult: {schema: , _value_1: ANY}
#             NewsInfoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> NewsInfoXMLResult: {_value_1: ANY}
#             OmodInfoXML() -> OmodInfoXMLResult: {_value_1: ANY}
#             OstatDepo(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDepoResult: {schema: , _value_1: ANY}
#             OstatDepoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDepoXMLResult: {_value_1: ANY}
#             OstatDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDynamicResult: {schema: , _value_1: ANY}
#             OstatDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDynamicXMLResult: {_value_1: ANY}
#             Overnight(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OvernightResult: {schema: , _value_1: ANY}
#             OvernightXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OvernightXMLResult: {_value_1: ANY}
#             ROISfix(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ROISfixResult: {schema: , _value_1: ANY}
#             ROISfixXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ROISfixXMLResult: {_value_1: ANY}
#             RepoDebtUSD(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RepoDebtUSDResult: {schema: , _value_1: ANY}
#             RepoDebtUSDXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RepoDebtUSDXMLResult: {_value_1: ANY}
#             Repo_debt(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Repo_debtResult: {schema: , _value_1: ANY}
#             Repo_debtXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Repo_debtXMLResult: {_value_1: ANY}
#             Ruonia(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RuoniaResult: {schema: , _value_1: ANY}
#             RuoniaXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RuoniaXMLResult: {_value_1: ANY}
#             Saldo(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SaldoResult: {schema: , _value_1: ANY}
#             SaldoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SaldoXMLResult: {_value_1: ANY}
#             SwapDayTotal(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDayTotalResult: {schema: , _value_1: ANY}
#             SwapDayTotalXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDayTotalXMLResult: {_value_1: ANY}
#             SwapDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDynamicResult: {schema: , _value_1: ANY}
#             SwapDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDynamicXMLResult: {_value_1: ANY}
#             SwapInfoSellUSD(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDResult: {schema: , _value_1: ANY}
#             SwapInfoSellUSDVol(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDVolResult: {schema: , _value_1: ANY}
#             SwapInfoSellUSDVolXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDVolXMLResult: {_value_1: ANY}
#             SwapInfoSellUSDXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDXMLResult: {_value_1: ANY}
#             SwapMonthTotal(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapMonthTotalResult: {schema: , _value_1: ANY}
#             SwapMonthTotalXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapMonthTotalXMLResult: {_value_1: ANY}
#             ValIntDay(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ValIntDayResult: {schema: , _value_1: ANY}
#             ValIntDayXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ValIntDayXMLResult: {_value_1: ANY}
#             XVol(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> XVolResult: {schema: , _value_1: ANY}
#             XVolXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> XVolXMLResult: {_value_1: ANY}
#             mrrf(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrfResult: {schema: , _value_1: ANY}
#             mrrf7D(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrf7DResult: {schema: , _value_1: ANY}
#             mrrf7DXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrf7DXMLResult: {_value_1: ANY}
#             mrrfXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrfXMLResult: {_value_1: ANY}
#
#      Port: DailyInfoSoap12 (Soap12Binding: {http://web.cbr.ru/}DailyInfoSoap12)
#          Operations:
#             AllDataInfoXML() -> AllDataInfoXMLResult: {_value_1: ANY}
#             Bauction(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BauctionResult: {schema: , _value_1: ANY}
#             BauctionXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BauctionXMLResult: {_value_1: ANY}
#             BiCurBacket() -> BiCurBacketResult: {schema: , _value_1: ANY}
#             BiCurBacketXML() -> BiCurBacketXMLResult: {_value_1: ANY}
#             BiCurBase(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BiCurBaseResult: {schema: , _value_1: ANY}
#             BiCurBaseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> BiCurBaseXMLResult: {_value_1: ANY}
#             Coins_base(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Coins_baseResult: {schema: , _value_1: ANY}
#             Coins_baseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Coins_baseXMLResult: {_value_1: ANY}
#             DV(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DVResult: {schema: , _value_1: ANY}
#             DVXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DVXMLResult: {_value_1: ANY}
#             DepoDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DepoDynamicResult: {schema: , _value_1: ANY}
#             DepoDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DepoDynamicXMLResult: {_value_1: ANY}
#             DragMetDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DragMetDynamicResult: {schema: , _value_1: ANY}
#             DragMetDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> DragMetDynamicXMLResult: {_value_1: ANY}
#             EnumReutersValutes() -> EnumReutersValutesResult: {schema: , _value_1: ANY}
#             EnumReutersValutesXML() -> EnumReutersValutesXMLResult: {_value_1: ANY}
#             EnumValutes(Seld: xsd:boolean) -> EnumValutesResult: {schema: , _value_1: ANY}
#             EnumValutesXML(Seld: xsd:boolean) -> EnumValutesXMLResult: {_value_1: ANY}
#             FixingBase(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> FixingBaseResult: {schema: , _value_1: ANY}
#             FixingBaseXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> FixingBaseXMLResult: {_value_1: ANY}
#             GetCursDynamic(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string) -> GetCursDynamicResult: {schema: , _value_1: ANY}
#             GetCursDynamicXML(FromDate: xsd:dateTime, ToDate: xsd:dateTime, ValutaCode: xsd:string) -> GetCursDynamicXMLResult: {_value_1: ANY}
#             GetCursOnDate(On_date: xsd:dateTime) -> GetCursOnDateResult: {schema: , _value_1: ANY}
#             GetCursOnDateXML(On_date: xsd:dateTime) -> GetCursOnDateXMLResult: {_value_1: ANY}
#             GetLatestDate() -> GetLatestDateResult: xsd:string
#             GetLatestDateSeld() -> GetLatestDateSeldResult: xsd:string
#             GetLatestDateTime() -> GetLatestDateTimeResult: xsd:dateTime
#             GetLatestDateTimeSeld() -> GetLatestDateTimeSeldResult: xsd:dateTime
#             GetLatestReutersDateTime() -> GetLatestReutersDateTimeResult: xsd:dateTime
#             GetReutersCursDynamic(FromDate: xsd:dateTime, ToDate: xsd:dateTime, NumCode: xsd:int) -> GetReutersCursDynamicResult: {schema: , _value_1: ANY}
#             GetReutersCursDynamicXML(FromDate: xsd:dateTime, ToDate: xsd:dateTime, NumCode: xsd:int) -> GetReutersCursDynamicXMLResult: {_value_1: ANY}
#             GetReutersCursOnDate(On_date: xsd:dateTime) -> GetReutersCursOnDateResult: {schema: , _value_1: ANY}
#             GetReutersCursOnDateXML(On_date: xsd:dateTime) -> GetReutersCursOnDateXMLResult: {_value_1: ANY}
#             GetSeldCursOnDate(On_date: xsd:dateTime) -> GetSeldCursOnDateResult: {schema: , _value_1: ANY}
#             GetSeldCursOnDateXML(On_date: xsd:dateTime) -> GetSeldCursOnDateXMLResult: {_value_1: ANY}
#             KeyRate(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> KeyRateResult: {schema: , _value_1: ANY}
#             KeyRateXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> KeyRateXMLResult: {_value_1: ANY}
#             MKR(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> MKRResult: {schema: , _value_1: ANY}
#             MKRXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> MKRXMLResult: {_value_1: ANY}
#             MainInfoXML() -> MainInfoXMLResult: {_value_1: ANY}
#             NewsInfo(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> NewsInfoResult: {schema: , _value_1: ANY}
#             NewsInfoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> NewsInfoXMLResult: {_value_1: ANY}
#             OmodInfoXML() -> OmodInfoXMLResult: {_value_1: ANY}
#             OstatDepo(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDepoResult: {schema: , _value_1: ANY}
#             OstatDepoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDepoXMLResult: {_value_1: ANY}
#             OstatDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDynamicResult: {schema: , _value_1: ANY}
#             OstatDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OstatDynamicXMLResult: {_value_1: ANY}
#             Overnight(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OvernightResult: {schema: , _value_1: ANY}
#             OvernightXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> OvernightXMLResult: {_value_1: ANY}
#             ROISfix(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ROISfixResult: {schema: , _value_1: ANY}
#             ROISfixXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ROISfixXMLResult: {_value_1: ANY}
#             RepoDebtUSD(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RepoDebtUSDResult: {schema: , _value_1: ANY}
#             RepoDebtUSDXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RepoDebtUSDXMLResult: {_value_1: ANY}
#             Repo_debt(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Repo_debtResult: {schema: , _value_1: ANY}
#             Repo_debtXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> Repo_debtXMLResult: {_value_1: ANY}
#             Ruonia(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RuoniaResult: {schema: , _value_1: ANY}
#             RuoniaXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> RuoniaXMLResult: {_value_1: ANY}
#             Saldo(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SaldoResult: {schema: , _value_1: ANY}
#             SaldoXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SaldoXMLResult: {_value_1: ANY}
#             SwapDayTotal(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDayTotalResult: {schema: , _value_1: ANY}
#             SwapDayTotalXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDayTotalXMLResult: {_value_1: ANY}
#             SwapDynamic(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDynamicResult: {schema: , _value_1: ANY}
#             SwapDynamicXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapDynamicXMLResult: {_value_1: ANY}
#             SwapInfoSellUSD(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDResult: {schema: , _value_1: ANY}
#             SwapInfoSellUSDVol(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDVolResult: {schema: , _value_1: ANY}
#             SwapInfoSellUSDVolXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDVolXMLResult: {_value_1: ANY}
#             SwapInfoSellUSDXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapInfoSellUSDXMLResult: {_value_1: ANY}
#             SwapMonthTotal(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapMonthTotalResult: {schema: , _value_1: ANY}
#             SwapMonthTotalXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> SwapMonthTotalXMLResult: {_value_1: ANY}
#             ValIntDay(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ValIntDayResult: {schema: , _value_1: ANY}
#             ValIntDayXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> ValIntDayXMLResult: {_value_1: ANY}
#             XVol(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> XVolResult: {schema: , _value_1: ANY}
#             XVolXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> XVolXMLResult: {_value_1: ANY}
#             mrrf(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrfResult: {schema: , _value_1: ANY}
#             mrrf7D(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrf7DResult: {schema: , _value_1: ANY}
#             mrrf7DXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrf7DXMLResult: {_value_1: ANY}
#             mrrfXML(fromDate: xsd:dateTime, ToDate: xsd:dateTime) -> mrrfXMLResult: {_value_1: ANY}
