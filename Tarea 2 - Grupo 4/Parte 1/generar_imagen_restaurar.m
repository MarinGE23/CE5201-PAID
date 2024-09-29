clear;clc; close all
pkg load image

% Imagen Original: I1
I1=imread('paisaje.jpg');
subplot(2,2,1)
imshow(I1)
title('(a) paisaje.jpg','FontSize',16)

% Texto: I2
I2=imread('marca.jpg');
I2(I2<50)=0; I2(I2>=50)=255; % Convertir imagen a Binaria. Parte Blanca = Texto. Parte Negra = Valor de 0
subplot(2,2,2)
imshow(I2)
title('(b) marca.jpg','FontSize',16)

% Imagen a Restaurar: I3
I3=I1+I2;
subplot(2,2,3)
imshow(I3)
title('(c) Imagen a Restaurar','FontSize',16)

% Restaurar
I4 = im2double(I3);

% Definir la mascara de la region afectada (1: texto blanco, 0: fondo)
mask_ohm = I4 > 0.98;  % Asumir que el texto es de color blanco, umbral alto
%mask_ohm = mask_ohm(10:310, 10:652);

% Definir kernels de difusion
kernel1 = [0.073235 0.176765 0.073235;
           0.176765 0        0.176765;
           0.073235 0.176765 0.073235];

kernel2 = [0.125 0.125 0.125;
           0.125 0     0.125;
           0.125 0.125 0.125];

% Numero de iteraciones del proceso de difusion
num_iterations = 10;
for iter=1:num_iterations
    % Aplicar convolucion a la imagen con el kernel
    smoothed_img = conv2(I4, kernel2, 'same');

    % Restaurar solo los pixeles dentro de la region afectada (el texto blanco)
    I4(mask_ohm == 1) = smoothed_img(mask_ohm == 1);

    % Visualizar el proceso de restauracion cada ciertas iteraciones
    %figure;
    %imshow(I4);
    %title(['Iteración: ', num2str(iter)]);
    %pause(0.5);
end

% Imagen Restaurada: I4
I4 = im2uint8(I4);
subplot(2,2,4)
imshow(I4)
title('(d) Imagen Restaurada','FontSize',16)

result = ssim(I1, I4);
disp(['SSIM entre Imagen Original e Imagen Restaurada: ', num2str(result)]);
