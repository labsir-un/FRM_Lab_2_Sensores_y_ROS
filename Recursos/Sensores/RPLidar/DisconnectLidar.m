% Switches off Laser and Closes Serial Comm Link
fprintf(lidar,'QT');
fclose(lidar);
close all;