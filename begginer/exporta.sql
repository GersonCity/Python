exec PKG_WEBBPR$Clear_tables 
go
exec [GRPI_CERT]..sp_procedure_params_rowset N'PKG_WEBBPR$Clear_tables',1,NULL,NULL
go
exec PKG_WEBBPR$Carga_Usuario @PFECHA=N'20180228',@PRUT=4139
go
 set quoted_identifier off 
go
 set fmtonly on select * from GRPI_CERT.dbo.USUARIO_RELACIONADO where 1=2 set fmtonly off
go
 set fmtonly off
go
exec [sys].sp_bcp_dbcmptlevel GRPI_CERT set fmtonly on select * from GRPI_CERT.dbo.USUARIO_RELACIONADO set fmtonly off
go
 exec GRPI_CERT.[sys].sp_tablecollations_100 'GRPI_CERT.dbo.USUARIO_RELACIONADO'
go
select [usu_rut],[ure_rut_relacionado] from GRPI_CERT.dbo.USUARIO_RELACIONADO
go
 set quoted_identifier off 
go
 set fmtonly on select * from GRPI_CERT.dbo.EQUIVALENCIA where 1=2 set fmtonly off
go
 set fmtonly off
go


