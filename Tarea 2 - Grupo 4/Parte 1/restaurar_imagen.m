clear;clc; close all
pkg load image

% Definir kernels de difusion
global kernel1;
global kernel2;
kernel1 = [0.073235 0.176765 0.073235;
           0.176765 0        0.176765;
           0.073235 0.176765 0.073235];

kernel2 = [0.125 0.125 0.125;
           0.125 0     0.125;
           0.125 0.125 0.125];

function restaurar_imagen(imagen_original, imagen_binaria, num_iterations)
    % Crear nueva ventana
    figure;
    global kernel1;
    global kernel2;

    % Leer Imagen Original
    I1 = imread(imagen_original);
    subplot(1,3,1)
    imshow(I1)
    title(['(a) ', imagen_original],'FontSize',16)

    % Leer Imagen Binaria
    I2 = imread(imagen_binaria);
    I2(I2<50)=0; I2(I2>=50)=255; % Convertir imagen a Binaria
    subplot(1,3,2)
    imshow(I2)
    title(['(b) ', imagen_binaria],'FontSize',16)

    % Imagen a Restaurar: I3
    I3 = I1;
    for c=1:3
        I3(:,:,c) = I1(:,:,c) + I2;  % Añadir la marca en cada canal
    end

    % Restaurar
    I4 = im2double(I3);

    % Definir la mascara de la region afectada (1: fondo blanco, 0: fondo negro)
    mask_ohm = I2 > 0.98;

    % Proceso de difusion iterativo
    for iter=1:num_iterations
        for c=1:3
            % Aplicar convolucion a la imagen con el kernel
            smoothed_img = conv2(I4(:,:,c), kernel2, 'same');

            % Crear una copia del canal que se va a modificar
            current_channel = I4(:,:,c);

            % Restaurar solo los pixeles dentro de la region afectada (fondo blanco)
            current_channel(mask_ohm == 1) = smoothed_img(mask_ohm == 1);

            % Asignar el canal restaurado de vuelta a la imagen
            I4(:,:,c) = current_channel;
        end
    end

    % Imagen Restaurada: I4
    I4 = im2uint8(I4);
    subplot(1,3,3)
    imshow(I4)
    title('(c) Imagen Restaurada','FontSize',16)

    % Calcular SSIM entre la imagen original y la imagen restaurada para cada canal
    ssim_r = ssim(I1(:,:,1), I4(:,:,1));
    ssim_g = ssim(I1(:,:,2), I4(:,:,2));
    ssim_b = ssim(I1(:,:,3), I4(:,:,3));

    % Promedio del SSIM entre los canales
    ssim_avg = mean([ssim_r, ssim_g, ssim_b]);

    disp(['SSIM entre Imagen Original e Imagen Restaurada: ', num2str(ssim_avg)]);
end

% Llamar a la funcion tres veces con diferentes imagenes
restaurar_imagen('persona1.jpg', 'binario1.jpg', 1000);
restaurar_imagen('persona2.jpg', 'binario2.jpg', 1000);
restaurar_imagen('persona3.jpg', 'binario3.jpg', 1000);
