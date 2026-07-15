-- extrae las gestantes unicas por dia sin repetir anteriores
use DGEMPRES50;

DECLARE @from DATETIME = '20260528', @to DATETIME = '20260529';

;WITH 
	CIE_BAI AS (
		SELECT *
		FROM (VALUES

		('O021','gestante'),
		('O030','gestante'),
		('O031','gestante'),
		('O032','gestante'),
		('O033','gestante'),
		('O034','gestante'),
		('O035','gestante'),
		('O036','gestante'),
		('O037','gestante'),
		('O038','gestante'),
		('O039','gestante'),
		('O040','gestante'),
		('O041','gestante'),
		('O042','gestante'),
		('O043','gestante'),
		('O044','gestante'),
		('O045','gestante'),
		('O046','gestante'),
		('O047','gestante'),
		('O048','gestante'),
		('O049','gestante'),
		('O050','gestante'),
		('O051','gestante'),
		('O052','gestante'),
		('O053','gestante'),
		('O054','gestante'),
		('O055','gestante'),
		('O056','gestante'),
		('O057','gestante'),
		('O058','gestante'),
		('O059','gestante'),
		('O060','gestante'),
		('O061','gestante'),
		('O062','gestante'),
		('O063','gestante'),
		('O064','gestante'),
		('O065','gestante'),
		('O066','gestante'),
		('O067','gestante'),
		('O068','gestante'),
		('O069','gestante'),
		('O070','gestante'),
		('O071','gestante'),
		('O072','gestante'),
		('O073','gestante'),
		('O074','gestante'),
		('O075','gestante'),
		('O076','gestante'),
		('O077','gestante'),
		('O078','gestante'),
		('O079','gestante'),
		('O200','gestante'),
		('O311','gestante'),
		('Z351','gestante'),
		('O470','gestante'),
		('O471','gestante'),
		('O479','gestante'),
		('O610','gestante'),
		('O611','gestante'),
		('O620','gestante'),
		('O621','gestante'),
		('O623','gestante'),
		('O624','gestante'),
		('O629','gestante'),
		('O630','gestante'),
		('O631','gestante'),
		('O639','gestante'),
		('O755','gestante'),
		('O756','gestante'),
		('O262','gestante'),
		('O280','gestante'),
		('O281','gestante'),
		('O282','gestante'),
		('O283','gestante'),
		('O284','gestante'),
		('O285','gestante'),
		('O288','gestante'),
		('O289','gestante'),
		('O320','gestante'),
		('O321','gestante'),
		('O322','gestante'),
		('O323','gestante'),
		('O324','gestante'),
		('O325','gestante'),
		('O326','gestante'),
		('O328','gestante'),
		('O329','gestante'),
		('O330','gestante'),
		('O331','gestante'),
		('O332','gestante'),
		('O333','gestante'),
		('O334','gestante'),
		('O335','gestante'),
		('O336','gestante'),
		('O337','gestante'),
		('O338','gestante'),
		('O339','gestante'),
		('O340','gestante'),
		('O341','gestante'),
		('O342','gestante'),
		('O343','gestante'),
		('O344','gestante'),
		('O345','gestante'),
		('O346','gestante'),
		('O347','gestante'),
		('O348','gestante'),
		('O349','gestante'),
		('O350','gestante'),
		('O351','gestante'),
		('O352','gestante'),
		('O353','gestante'),
		('O354','gestante'),
		('O355','gestante'),
		('O356','gestante'),
		('O357','gestante'),
		('O358','gestante'),
		('O359','gestante'),
		('O360','gestante'),
		('O361','gestante'),
		('O362','gestante'),
		('O363','gestante'),
		('O365','gestante'),
		('O366','gestante'),
		('O368','gestante'),
		('O369','gestante'),
		('O290','gestante'),
		('O291','gestante'),
		('O292','gestante'),
		('O293','gestante'),
		('O294','gestante'),
		('O295','gestante'),
		('O298','gestante'),
		('O299','gestante'),
		('O740','gestante'),
		('O741','gestante'),
		('O742','gestante'),
		('O743','gestante'),
		('O744','gestante'),
		('O745','gestante'),
		('O746','gestante'),
		('O748','gestante'),
		('O749','gestante'),
		('O890','gestante'),
		('O891','gestante'),
		('O892','gestante'),
		('O893','gestante'),
		('O894','gestante'),
		('O895','gestante'),
		('O898','gestante'),
		('O899','gestante'),
		('O690','gestante'),
		('O691','gestante'),
		('O692','gestante'),
		('O693','gestante'),
		('O694','gestante'),
		('O695','gestante'),
		('O698','gestante'),
		('O699','gestante'),
		('O901','gestante'),
		('O902','gestante'),
		('O903','gestante'),
		('O904','gestante'),
		('O905','gestante'),
		('O908','gestante'),
		('O909','gestante'),
		('Z390','gestante'),
		('Z391','gestante'),
		('Z392','gestante'),
		('Z320','gestante'),
		('Z321','gestante'),
		('Z33X','gestante'),
		('Z340','gestante'),
		('Z348','gestante'),
		('Z349','gestante'),
		('Z350','gestante'),
		('Z352','gestante'),
		('Z353','gestante'),
		('Z354','gestante'),
		('Z357','gestante'),
		('Z358','gestante'),
		('Z359','gestante'),
		('Z360','gestante'),
		('Z361','gestante'),
		('Z363','gestante'),
		('Z364','gestante'),
		('Z365','gestante'),
		('Z369','gestante'),
		('O000','gestante'),
		('O001','gestante'),
		('O002','gestante'),
		('O008','gestante'),
		('O009','gestante'),
		('O080','gestante'),
		('O081','gestante'),
		('O082','gestante'),
		('O083','gestante'),
		('O084','gestante'),
		('O085','gestante'),
		('O086','gestante'),
		('O087','gestante'),
		('O088','gestante'),
		('O089','gestante'),
		('O367','gestante'),
		('O833','gestante'),
		('O300','gestante'),
		('O301','gestante'),
		('O302','gestante'),
		('O309','gestante'),
		('O310','gestante'),
		('O318','gestante'),
		('O240','gestante'),
		('O241','gestante'),
		('O242','gestante'),
		('O243','gestante'),
		('O244','gestante'),
		('O249','gestante'),
		('O25X','gestante'),
		('O980','gestante'),
		('O981','gestante'),
		('O982','gestante'),
		('O983','gestante'),
		('O984','gestante'),
		('O985','gestante'),
		('O987','gestante'),
		('O988','gestante'),
		('O989','gestante'),
		('O990','gestante'),
		('O991','gestante'),
		('O993','gestante'),
		('O994','gestante'),
		('O995','gestante'),
		('O996','gestante'),
		('O998','gestante'),
		('O440','gestante'),
		('O441','gestante'),
		('O450','gestante'),
		('O459','gestante'),
		('O460','gestante'),
		('O469','gestante'),
		('O670','gestante'),
		('O679','gestante'),
		('O720','gestante'),
		('O722','gestante'),
		('O723','gestante'),
		('O730','gestante'),
		('O731','gestante'),
		('O209','gestante'),
		('O210','gestante'),
		('O211','gestante'),
		('O212','gestante'),
		('O219','gestante'),
		('O230','gestante'),
		('O231','gestante'),
		('O232','gestante'),
		('O233','gestante'),
		('O235','gestante'),
		('O264','gestante'),
		('O85X','gestante'),
		('O860','gestante'),
		('O861','gestante'),
		('O862','gestante'),
		('O864','gestante'),
		('O868','gestante'),
		('O911','gestante'),
		('O910','gestante'),
		('O912','gestante'),
		('O920','gestante'),
		('O921','gestante'),
		('O923','gestante'),
		('O924','gestante'),
		('O925','gestante'),
		('O926','gestante'),
		('O927','gestante'),
		('O40X','gestante'),
		('O410','gestante'),
		('O411','gestante'),
		('O418','gestante'),
		('O419','gestante'),
		('O010','gestante'),
		('O011','gestante'),
		('O019','gestante'),
		('O020','gestante'),
		('O028','gestante'),
		('O029','gestante'),
		('O109','gestante'),
		('O208','gestante'),
		('O218','gestante'),
		('O228','gestante'),
		('O229','gestante'),
		('O234','gestante'),
		('O239','gestante'),
		('O260','gestante'),
		('O261','gestante'),
		('O263','gestante'),
		('O265','gestante'),
		('O266','gestante'),
		('O267','gestante'),
		('O268','gestante'),
		('O269','gestante'),
		('O296','gestante'),
		('O308','gestante'),
		('O438','gestante'),
		('O458','gestante'),
		('O468','gestante'),
		('O618','gestante'),
		('O619','gestante'),
		('O622','gestante'),
		('O628','gestante'),
		('O632','gestante'),
		('O668','gestante'),
		('O678','gestante'),
		('O715','gestante'),
		('O718','gestante'),
		('O721','gestante'),
		('O747','gestante'),
		('O751','gestante'),
		('O752','gestante'),
		('O753','gestante'),
		('O754','gestante'),
		('O758','gestante'),
		('O759','gestante'),
		('O815','gestante'),
		('O839','gestante'),
		('O848','gestante'),
		('O863','gestante'),
		('O878','gestante'),
		('O879','gestante'),
		('O896','gestante'),
		('O922','gestante'),
		('O960','gestante'),
		('O961','gestante'),
		('O969','gestante'),
		('O970','gestante'),
		('O971','gestante'),
		('O979','gestante'),
		('O97X','gestante'),
		('O986','gestante'),
		('O992','gestante'),
		('O997','gestante'),
		('Z355','gestante'),
		('Z356','gestante'),
		('Z362','gestante'),
		('Z368','gestante'),
		('Z640','gestante'),
		('Z875','gestante'),
		('Z876','gestante'),
		('O757','gestante'),
		('O820','gestante'),
		('O821','gestante'),
		('O822','gestante'),
		('O828','gestante'),
		('O829','gestante'),
		('O842','gestante'),
		('O900','gestante'),
		('O420','gestante'),
		('O421','gestante'),
		('O422','gestante'),
		('O429','gestante'),
		('O48X','gestante'),
		('O603','gestante'),
		('O60X','gestante'),
		('Z370','gestante'),
		('Z372','gestante'),
		('Z374','gestante'),
		('Z375','gestante'),
		('Z376','gestante'),
		('Z377','gestante'),
		('Z379','gestante'),
		('Z380','gestante'),
		('Z381','gestante'),
		('Z382','gestante'),
		('Z383','gestante'),
		('Z384','gestante'),
		('Z385','gestante'),
		('Z386','gestante'),
		('Z387','gestante'),
		('Z388','gestante'),
		('O680','gestante'),
		('O681','gestante'),
		('O682','gestante'),
		('O683','gestante'),
		('O688','gestante'),
		('O689','gestante'),
		('O750','gestante'),
		('O800','gestante'),
		('O801','gestante'),
		('O808','gestante'),
		('O809','gestante'),
		('O810','gestante'),
		('O811','gestante'),
		('O812','gestante'),
		('O813','gestante'),
		('O814','gestante'),
		('O830','gestante'),
		('O831','gestante'),
		('O832','gestante'),
		('O834','gestante'),
		('O838','gestante'),
		('O840','gestante'),
		('O841','gestante'),
		('O849','gestante'),
		('O640','gestante'),
		('O641','gestante'),
		('O642','gestante'),
		('O643','gestante'),
		('O644','gestante'),
		('O645','gestante'),
		('O648','gestante'),
		('O649','gestante'),
		('O650','gestante'),
		('O651','gestante'),
		('O652','gestante'),
		('O653','gestante'),
		('O654','gestante'),
		('O655','gestante'),
		('O658','gestante'),
		('O659','gestante'),
		('O660','gestante'),
		('O661','gestante'),
		('O662','gestante'),
		('O663','gestante'),
		('O664','gestante'),
		('O665','gestante'),
		('O669','gestante'),
		('O100','gestante'),
		('O101','gestante'),
		('O102','gestante'),
		('O103','gestante'),
		('O104','gestante'),
		('O11X','gestante'),
		('O120','gestante'),
		('O121','gestante'),
		('O122','gestante'),
		('O13X','gestante'),
		('O140','gestante'),
		('O141','gestante'),
		('O142','gestante'),
		('O149','gestante'),
		('O150','gestante'),
		('O151','gestante'),
		('O152','gestante'),
		('O159','gestante'),
		('O16X','gestante'),
		('O430','gestante'),
		('O431','gestante'),
		('O432','gestante'),
		('O439','gestante'),
		('O700','gestante'),
		('O701','gestante'),
		('O702','gestante'),
		('O703','gestante'),
		('O709','gestante'),
		('O710','gestante'),
		('O711','gestante'),
		('O712','gestante'),
		('O713','gestante'),
		('O714','gestante'),
		('O716','gestante'),
		('O717','gestante'),
		('O220','gestante'),
		('O221','gestante'),
		('O222','gestante'),
		('O223','gestante'),
		('O224','gestante'),
		('O225','gestante'),
		('O870','gestante'),
		('O871','gestante'),
		('O872','gestante'),
		('O873','gestante'),
		('O880','gestante'),
		('O881','gestante'),
		('O882','gestante'),
		('O883','gestante'),
		('O888','gestante'),
		('O312','gestante'),
		('O364','gestante'),
		('O93X','gestante'),
		('O95X','gestante'),
		('O96X','gestante'),
		('Z371','gestante'),
		('Z373','gestante')


		) AS V (COD, NOMBRE)
	),

bai_init as (

	SELECT DISTINCT
		GENPACIEN.PACNUMDOC
		, CIE_BAI.NOMBRE EVENTO
		, CONCAT(ADNINGRESO.AINCONSEC, CIE_BAI.NOMBRE) llave
		, 'antiguo' etiqueta 
	FROM ADNINGRESO
		INNER JOIN GENPACIEN ON ADNINGRESO.GENPACIEN = GENPACIEN.OID
		INNER JOIN HCNFOLIO ON HCNFOLIO.ADNINGRESO = ADNINGRESO.OID
		INNER JOIN HCNDIAPAC ON HCNFOLIO.OID = HCNDIAPAC.HCNFOLIO
		INNER JOIN GENDIAGNO ON GENDIAGNO.OID = HCNDIAPAC.GENDIAGNO
		INNER JOIN CIE_BAI ON GENDIAGNO.DIACODIGO = CIE_BAI.COD
	WHERE HCNFOLIO.HCFECFOL BETWEEN CONVERT(DATETIME, '20260528', 120) AND DATEADD(day, -1, CONVERT(DATETIME, @to, 120))
	),

bai_fin as (
	SELECT DISTINCT
		GENPACIEN.PACNUMDOC
		, CIE_BAI.NOMBRE EVENTO
		, CONCAT(ADNINGRESO.AINCONSEC, CIE_BAI.NOMBRE) llave
		, FORMAT(HCNFOLIO.HCFECFOL, 'yyyy-MM-dd HH:mm', 'en-us') AS FECHA_DX
		, GENDIAGNO.DIACODIGO AS DX
		, DATEDIFF(YEAR, GENPACIEN.GPAFECNAC, ADNINGRESO.AINFECING) - CASE WHEN (MONTH(GENPACIEN.GPAFECNAC) > MONTH(ADNINGRESO.AINFECING) OR  (MONTH(GENPACIEN.GPAFECNAC) = MONTH(ADNINGRESO.AINFECING) AND DAY(GENPACIEN.GPAFECNAC) > DAY(ADNINGRESO.AINFECING))) THEN 1 ELSE 0 END AS EDAD
		, GENDIAGNO.DIANOMBRE AS Descripciónes_CIE_X_diagnóstico_relacionado
		, GENARESER.GASNOMBRE AS AREA
		, HCNTIPHIS.HCCODIGO AS COD_FOLIO
		, HCNTIPHIS.HCNOMBRE AS NOMBRE_FOLIO
		, GENMEDICO.GMENOMCOM
		, GENESPECI.GEEDESCRI
		, GENPACIEN.PACPRINOM AS PRIMER_NOMBRE
		, GENPACIEN.PACSEGNOM AS SEGUNDO_NOMBRE
		, GENPACIEN.PACPRIAPE AS PRIMER_APELLIDO
		, GENPACIEN.PACSEGAPE AS SEGUNDO_APELLIDO
		, CASE GENPACIEN.PACTIPDOC WHEN 1 THEN 'CC' WHEN 2 THEN 'CE' WHEN 3 THEN 'TI' WHEN 4 THEN 'RC' WHEN 5 THEN 'PA' WHEN 6 THEN 'AS' WHEN 7 THEN 'MS' WHEN 8 THEN 'NU' WHEN 10 THEN 'CN' WHEN 12 THEN 'PE' WHEN 14 THEN 'PE' WHEN 15 THEN 'PE' WHEN 9 THEN 'PE'
			ELSE 'NONE' END AS Tipo
		, ADNGRUETN.ADGENOMBRE AS Etnia
			-- Ubiacion geografica
		, GENPAISES.gpanombre AS Pais
		, GENMUNICI.MUNNOMMUN AS Municipio
		, GENBARRIO.GEBNOMBRE AS Barrio
		, TRY_CAST(adinfpaci AS XML).value('(/HCCLInfoPaciente/@DIRECC)[1]', 'nvarchar(400)') AS [Direccion]
		, CASE GENBARRIO.GEBZONAUR WHEN 0 THEN 'Urbana' WHEN 1 THEN 'Rural' WHEN 2 THEN 'Rural' else 'Ninguna' end as Zona
		, TRY_CAST(adinfpaci AS XML).value('(/HCCLInfoPaciente/@TELEF)[1]', 'nvarchar(400)') AS [Telefono]
		
		, FORMAT(GENPACIEN.GPAFECNAC, 'yyyy-MM-dd', 'en-us') AS FECHA_NACI
		, CASE GENDETCON.GDETIPREG WHEN 0 THEN 'Ninguno' WHEN 1 THEN 'Contributivo' WHEN 2 THEN 'Subsidiado' WHEN 3 THEN 'Excepción' WHEN 4 THEN 'Especial' WHEN 5 THEN 'No asegurado' END as [Tipo Regimen]
		, GENDETCON.GDENOMBRE [Nombre EAPB] 
		, CONVERT(CHAR(10), ADNINGRESO.ainfecing, 103) FECHA_INGRESO
		, CONVERT(CHAR(8),  ADNINGRESO.ainfecing, 108) HORA_INGRESO
	FROM ADNINGRESO
		INNER JOIN GENPACIEN ON ADNINGRESO.GENPACIEN = GENPACIEN.OID
		INNER JOIN HCNFOLIO ON HCNFOLIO.ADNINGRESO = ADNINGRESO.OID
		INNER JOIN HCNDIAPAC ON HCNFOLIO.OID = HCNDIAPAC.HCNFOLIO
		INNER JOIN GENDIAGNO ON GENDIAGNO.OID = HCNDIAPAC.GENDIAGNO
		INNER JOIN CIE_BAI ON GENDIAGNO.DIACODIGO = CIE_BAI.COD
		LEFT JOIN GENARESER on HCNFOLIO.GENARESER =  GENARESER.OID
		LEFT JOIN GENMEDICO ON HCNFOLIO.GENMEDICO = GENMEDICO.OID
		LEFT JOIN GENESPECI on HCNFOLIO.GENESPECI = GENESPECI.OID
		LEFT JOIN HCNTIPHIS on HCNFOLIO.HCNTIPHIS = HCNTIPHIS.OID
		LEFT JOIN ADNGRUETN ON GENPACIEN.ADNGRUETN = ADNGRUETN.ADGGRUETN
		LEFT JOIN GENPAISES ON GENPACIEN.GENPAIS = GENPAISES.OID
		LEFT JOIN GENMUNICI ON GENPACIEN.DGNMUNICIPIO = GENMUNICI.OID
		LEFT JOIN GENBARRIO ON GENPACIEN.GENBARRIO = GENBARRIO.OID
		LEFT JOIN GENDETCON ON GENDETCON.OID = GENPACIEN.GENDETCON 

	WHERE HCNFOLIO.HCFECFOL BETWEEN CONVERT(DATETIME, @from, 120) AND CONVERT(DATETIME, @to, 120)
	),

bai_concat as (
	select 
		bai_fin.PACNUMDOC
		, bai_fin.llave
		, bai_init.etiqueta
		, bai_fin.FECHA_DX
		, bai_fin.EVENTO
		, bai_fin.DX
		, bai_fin.EDAD
		, bai_fin.Descripciónes_CIE_X_diagnóstico_relacionado
		, bai_fin.AREA
		, bai_fin.COD_FOLIO
		, bai_fin.NOMBRE_FOLIO
		, bai_fin.GMENOMCOM
		, bai_fin.GEEDESCRI
		, ROW_NUMBER() OVER (PARTITION BY concat(bai_fin.PACNUMDOC, bai_fin.EVENTO) ORDER BY bai_fin.FECHA_DX ASC) rn
		, bai_fin.PRIMER_NOMBRE
		, bai_fin.SEGUNDO_NOMBRE
		, bai_fin.PRIMER_APELLIDO
		, bai_fin.SEGUNDO_APELLIDO
		, bai_fin.Tipo
		, bai_fin.Etnia
		, bai_fin.Pais
		, bai_fin.Municipio
		, bai_fin.Barrio
		, bai_fin.Direccion
		, bai_fin.Zona
		, bai_fin.Telefono
		, bai_fin.FECHA_NACI
		, bai_fin.[Tipo Regimen]
		, bai_fin.[Nombre EAPB] 
		, bai_fin.FECHA_INGRESO
		, bai_fin.HORA_INGRESO
	from bai_fin
		left join bai_init on bai_fin.llave = bai_init.llave

),

bai_selec as (
	SELECT *
	FROM bai_concat
 )
 SELECT DISTINCT
	PACNUMDOC Número
	, EVENTO
	, DX
	, PRIMER_NOMBRE
	, SEGUNDO_NOMBRE
	, PRIMER_APELLIDO
	, SEGUNDO_APELLIDO
	, Tipo
	, PACNUMDOC TIPO_ID
	, EDAD
	, UNIDAD_DE_MEDIDA = 0
	, REVISAR_HC = 0
	, Cumple_con_la_definicion_de_caso_del_evento	= 0
	, Notificado_al_Sivigila = 0
	, Toma_de_muestra = 0
	, Fecha_de_toma_de_muestra = 0
	, Resultado = 0
	, Clasificación_del_caso = 0
	, Observaciones = 0	
	, Descripciónes_CIE_X_diagnóstico_relacionado
	, CODIGO_DE_HABILITACON_DE_LA_IPS = '190010003101'
	, NOMBRE_COMPLETO_DE_LA_INSTITUCION_DE_SALUD = 'HOSPITAL UNIVERSITARIO SAN JOSE '
	, FECHA_DX
	--, llave
	--, etiqueta
	, AREA
	, COD_FOLIO
	, NOMBRE_FOLIO
	, GMENOMCOM
	, GEEDESCRI
	, Etnia
	--, rn
	, Pais
	, Municipio
	, Barrio
	, Direccion
	, Zona
	, Telefono
	, FECHA_NACI
	, [Tipo Regimen]
	, [Nombre EAPB]
	, FECHA_INGRESO
	, HORA_INGRESO

 FROM bai_selec
 where etiqueta IS NULL and rn = 1
 GROUP BY 
	PACNUMDOC  , llave
	, EVENTO
	, DX
	, PACNUMDOC 
	, etiqueta, FECHA_DX 
	, EDAD
	, Descripciónes_CIE_X_diagnóstico_relacionado
	, AREA
	, COD_FOLIO
	, NOMBRE_FOLIO
	, GMENOMCOM
	, GEEDESCRI
	, rn
	, PRIMER_NOMBRE
	, SEGUNDO_NOMBRE
	, PRIMER_APELLIDO
	, SEGUNDO_APELLIDO
	, Tipo
	, Etnia
	, Pais
	, Municipio
	, Barrio
	, Direccion
	, Zona
	, Telefono
	, FECHA_NACI
	, [Tipo Regimen]
	, [Nombre EAPB]
	, FECHA_INGRESO
	, HORA_INGRESO
ORDER BY PACNUMDOC ASC;