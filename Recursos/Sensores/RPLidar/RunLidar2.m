% RUNLIDAR2
% programa para ejecutar escaneos periódicos con el lidar HOKUYO URG-04LX,
% crea un archivo LIDARSET2 que contiene una fila de datos por cada
% escaneo. Se ejecutan 10 escaneos con separación de 6 segundos.
% Ricardo Ramírez Heredia. Universidad Nacional de Colombia. Usa el programa
% LidarScan  creado por Shikhar Shrestha, IIT Bhubaneswar.

%El lidar debe estar conectado y realizada la conexión con SetupLidar.

disp('Inicio escaneo')
LidarSet1=zeros(50,682);
for i=1:10
disp('Escaneo número:')
iplot
[rangescan]=LidarScan(lidar);
LidarSet2(i,:)=rangescan;
pause(6)
end
disp('Escaneo finalizado')