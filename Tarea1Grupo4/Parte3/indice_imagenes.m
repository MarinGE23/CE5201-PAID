clc; clear;
pkg load image;

function mse_val = mse(I, K)
    mse_val = mean((I(:) - K(:)).^2);
end

function psnr_val = psnr(I, K)
    mse_val = mse(I, K);
    max_I = max(I(:));
    psnr_val = 10 * log10(max_I^2 / mse_val);
end

function ssim_val = doublessim(I,K)
    ssim_val = ssim(I, K);
end

function snr_val = snr(I, K)
    signal_power = sum(I(:).^2);
    noise_power = sum((I(:) - K(:)).^2);
    snr_val = 10 * log10(signal_power / noise_power);
end

function c = hqi(A, B)
    % A y B son imágenes a escala de grises.
    % c es el valor de HQI.

    % Tamaño de la imagen
    [M, N] = size(A);

    % Obtener histogramas
    h_A = imhist(A);
    h_B = imhist(B);

    % Calcular el vector de diferencias Delta j
    delta_j = abs(h_A - h_B);

    % Calcular Delta TC
    Delta_TC = sum(delta_j);

    % Calcular Delta TC Factor
    Delta_TC_Factor = 1 - (Delta_TC / (2 * M * N));

    % Calcular HD (correlación entre histogramas)
    HD = sum(h_A .* h_B) / sum(h_A .^ 2);;

    % Calcular HQI
    c = Delta_TC_Factor * HD;
end


original = 'imOrig.jpg';
original_Image = imread(original);
files = dir('*.jpg');

fprintf('------------------------------------------------------------');
display('');
fprintf('|   Imagen   |'); fprintf('  MSE  |'); fprintf('  PSNR  |'); fprintf('  SSIM  |'); fprintf('  SNR  |'); fprintf('  HQI  |');
display('');
fprintf('------------------------------------------------------------');
display('');


for i = 1:length(files)-1
    filename = files(i).name;
    fprintf('| %s |', filename);


    mod_image = imread(filename);

    % Function calls
    fprintf('%d |', mse_val = mse(original_Image, mod_image));
    fprintf('%d |', psnr_val = psnr(original_Image, mod_image));
    fprintf('%d |', ssim_val = doublessim(original_Image, mod_image));
    fprintf('%d |', snr_val = snr(original_Image, mod_image));
    fprintf('%d |', c = hqi(original_Image, mod_image));



    display('');
    fprintf('------------------------------------------------------------');
    display('');
end
