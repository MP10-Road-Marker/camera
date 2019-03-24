function [centers, radius] = Acquire_center(low, high, T, S)
% cam = webcam  
% cam.Resolution = '800x600';
% cam.ExposureMode: 'manual'
% cam.Exposure = -10;
%cam.Resolution = '800x600';
%preview(cam)
%original_image = snapshot(cam);
original_image=imread('90cm_2_led.jpg');
figure,imshow(original_image);
%  
%Read image
cropped_image = imcrop(original_image,[300 150 200 300]);
%Crop the image into 200 in width and 300 in height
grayscale_image = rgb2gray(cropped_image);  
figure,imshow(grayscale_image);
figure
% Convert the original image into greyscale
[pixelCount, grayLevels] = imhist(grayscale_image); %Create a histogram of pixelcounts agains greylevels
bar(pixelCount); %Set pixel count to be bar chart
title('Histogram '); %Set a title
xlim([0 grayLevels(end)]); % Scale x axis manually.
grid on;
thresholdValue= T; %Set the threshold value
binary_image = grayscale_image < thresholdValue; %Binary thresholding-Bright objects will be chosen if you use <.
maxYValue = ylim;
line([thresholdValue, thresholdValue], maxYValue, 'Color', 'r')
%Draw the set threshold value label
annotationText = sprintf('Thresholded at %d gray levels', thresholdValue);
text(double(thresholdValue + 5), double(0.5 * maxYValue(2)), annotationText, 'FontSize', 10, 'Color', [0 .5 0]);
%Draw the backgound and foreground pixel labels
text(double(thresholdValue - 70), double(0.94 * maxYValue(2)), 'Background', 'FontSize', 10, 'Color', [0 0 .5]);
text(double(thresholdValue + 50), double(0.94 * maxYValue(2)), 'Foreground', 'FontSize', 10, 'Color', [0 0 .5]);
%figure, imshow(original_image);
%figure, imshow(grayscale_image);
%figure, imshow(binary_image);
%imtool(binary_image);
figure, imshow(cropped_image);
final_image = imresize(binary_image, [3000 2000]);% change the pixel density, the accuracy = 0.1mm
imtool(final_image);
di = imdistline; % radius range to search for the circles
delete(di);
[centers, radius] = imfindcircles(final_image, [low high], 'ObjectPolarity', 'dark','Sensitivity',S);
% find the circles with radius range 
figure,imshow(final_image);
h = viscircles (centers, radius);
% visualise the circle

end