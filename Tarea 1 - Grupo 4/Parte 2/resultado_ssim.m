clc; clear; close all;
pkg load image;
pkg load video;

function resultado_ssim()
  % Leer los videos
  V_original = VideoReader('original.mp4');
  V_alg1 = VideoReader('sin_ruido_alg1.mp4');
  V_alg2 = VideoReader('sin_ruido_alg2.mp4');

  fr = V_original.NumberOfFrames;  % Asumiendo que ambos videos tienen el mismo número de frames

  % Inicializar vectores para almacenar los valores de SSIM
  ssim_values_alg1 = zeros(fr, 1);
  ssim_values_alg2 = zeros(fr, 1);

  % Calcular SSIM para cada frame
  for k = 1:fr
      % Leer los frames correspondientes
      frame_original = readFrame(V_original);
      frame_alg1 = readFrame(V_alg1);
      frame_alg2 = readFrame(V_alg2);

      % Convertir los frames a escala de grises
      frame_original_gray = rgb2gray(frame_original);
      frame_alg1_gray = rgb2gray(frame_alg1);
      frame_alg2_gray = rgb2gray(frame_alg2);

      % Calcular SSIM entre el frame original y el filtrado con cada algoritmo
      ssim_values_alg1(k) = ssim(frame_original_gray, frame_alg1_gray);
      ssim_values_alg2(k) = ssim(frame_original_gray, frame_alg2_gray);
  end

  % Mostrar los resultados
  disp('SSIM promedio con Algoritmo 1:');
  disp(mean(ssim_values_alg1));
  disp('SSIM promedio con Algoritmo 2:');
  disp(mean(ssim_values_alg2));

  % Guardar los valores de SSIM en archivos para su posterior análisis
  save('ssim_values_alg1.mat', 'ssim_values_alg1');
  save('ssim_values_alg2.mat', 'ssim_values_alg2');
end

