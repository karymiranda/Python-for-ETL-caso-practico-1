import polars as pl

t_historico = pl.read_csv("..\GESTION DE ATENCIONES\Tickets\Tickets Historico.txt", separator=";")
t_historico.select(
    pl.col('Numero Ticket').alias('TicketID'),
    'Ubicacion',
    'Service Desk',
    'Estado',
    pl.col('Fecha Creacion').str.to_date(),
    pl.col('Fecha Termino').str.to_date(),
    pl.col('Fecha Cierre').str.to_date()
).head(10)

t_actual = pl.read_csv("..\GESTION DE ATENCIONES\Tickets\Tickets Actual.csv",separator='|')
t_actual.columns
t_actual.select(
    pl.col('Numero Ticket').alias('TicketID'),
    'Ubicacion',
    'Service Desk',
    'Estado',
    pl.col('Fecha Creacion').str.to_date(),
    pl.col('Fecha Termino').str.to_date(),
    pl.col('Fecha Cierre').str.to_date()
)

#Filtrar ticket que inicie con "WO"
t_actual.filter(
    pl.col('Numero Ticket').str.starts_with("WO")
    )