% RUNLIDAR1
% programa para ejecutar escaneos periódicos con el lidar HOKUYO URG-04LX,
% crea un archivo LIDARSET1 que contiene una fila de datos por cada
% escaneo. Se ejecutan 50 escaneos con separación de 10 segundos.
% Ricardo Ramírez Heredia. Universidad Nacional de Colombia. Usa el programa
% LidarScan  creado por Shikhar Shrestha, IIT Bhubaneswar, bajo Licencia
% GLP.

%El lidar debe estar conectado y realizada la conexión con SetupLidar.

disp('Inicio escaneo')
LidarSet1=zeros(3,682);
for i=1:3 %50
disp('Escaneo número:')
%iplot
[rangescan]=LidarScan(lidar);
LidarSet1(i,:)=rangescan;
pause(1)
end
disp('Escaneo finalizado')