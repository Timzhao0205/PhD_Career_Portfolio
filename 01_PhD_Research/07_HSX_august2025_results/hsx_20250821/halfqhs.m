clear; close all; clc;
files = dir('*.csv');
figure;

% only load files with name scope_ 62, 64, 66

% legend show;
x = [];
y = [];
% subplot 2,1,1;
% for i = 1:length(files)
%     if contains(files(i).name, 'scope_10')
%         % read the data from the csv file, read more decimal places
%         opts = detectImportOptions(files(i).name, 'NumHeaderLines', 0);
%         opts = setvartype(opts, 'double');
%         opts = setvaropts(opts, 'DecimalSeparator', '.');
%         data = readmatrix(files(i).name, opts);
%         % save scope_10.csv to x and y
%         x = data(4:end, 1);
%         y = data(4:end, 2);
        
%         % plot the data
%         subplot(1, 2, 1);
%         plot(x, y, 'linewidth', 1);
%         % add labels and title
%         xlabel('Time (s)');
%         xlim([0.83 0.89]);
%         ylim([0 0.6]);
%         hold on;
%         grid on;
%         grid minor;
%         %}
%         %{
%         % x is the time, y is the voltage. This is the time domain data. I would like to perform a fft analysis to the voltage using the time data from x
%         fs = 1/(x(10)-x(9)); % Sampling frequency
%         n = length(y); % Number of samples
%         f = fs*(0:(n/2))/n; % Frequency range
%         Y = fft(y); % FFT of the signal
%         P = abs(Y/n); % Normalize the FFT
%         P = P(1:n/2+1); % Keep only the positive frequencies
%         % is P in dB?
%         P_db = 20*log10(P);
%         % plot the FFT
%         plot(f, P);
%         % add labels and title
%         xlabel('Frequency (Hz)');
%         ylabel('Magnitude');
%         title(["One Tesla QHS Mode FFT, V_{bias} = 0.25 V"]);
%         xlim([24 6000]);
%         %}
%         %{
        
%         dt = x(10)-x(9);           % safer than x(10)-x(9)
%         fs = 1/dt;
%         Fs = 1 / (dt); % Calculate sampling frequency from your time data
%         L = length(y);         % Get the number of samples

%         Y = fft(y);            % Perform the Fast Fourier Transform

%         % Compute the two-sided spectrum P2, then the single-sided spectrum P1.
%         P2 = abs(Y/L);
%         P1 = P2(1:L/2+1);
%         P1(2:end-1) = 2*P1(2:end-1);

%         % 3. --- CONVERT TO dB AND CREATE FREQUENCY AXIS ---
%         P1_dB = 20*log10(P1);   % Convert the magnitude to decibels (dB)

%         % Define the frequency domain f
%         f = Fs*(0:(L/2))/L;
%         plot(f, P1_dB);
%         xlabel('Frequency (Hz)');
%         ylabel('Magnitude');
%         title(["One Tesla Low Elongation Mode FFT, V_{bias} = 0.4 V"]);
%         xlim([0 5000]);
%         %}
%     end
%     % create a new figure
    
%     % save the figure as a png file
    
% end
% save scope_10.csv to x and y
% bold every axes titles and increase font size to 12
% Shot 21
opts = detectImportOptions('scope_13.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double');
opts = setvaropts(opts, 'DecimalSeparator', '.');
data = readmatrix('scope_13.csv', opts);

% figWidth = 1200; 
% figHeight = 900;

% % 2. Create the figure and force the window size
% fig = figure('Color', 'w', 'Position', [100, 100, figWidth, figHeight]);
x = data(4:end, 1);
y = data(4:end, 2);

subplot(3,2 ,2);
hold on; box on;
plot(x, y, 'linewidth', 1);
% add labels and title
xlabel('Time (s)');
ylabel('Sensor Output (V)');
xlim([0.83 0.89]);
ylim([0 0.6]);
% title('Shot 21');
% grid on;
% grid minor;



data = readmatrix('./25_8_21_#21_stored_energy.dat');
x2 = data(:, 1);
y2 = data(:, 2);
subplot(3,2 ,1);

%Both data y and y2 should be somewhere directly proportional. However, the time data is messed up a little bit.
% Can you align the curvatures so that they overlap as much as possible?
plot(x2, y2, 'linewidth', 1, 'Color', [0.8500, 0.3250, 0.0980]);
xlim([0.8 0.86]);
ylim([-5 65]);
% grid on;
% grid minor;
% title('Shot 21');
xlabel('Time (s)');
ylabel('Stored Energy (J)');






% Shot 18
opts = detectImportOptions('scope_10.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double');
opts = setvaropts(opts, 'DecimalSeparator', '.');
data = readmatrix('scope_10.csv', opts);
x = data(4:end, 1);
y = data(4:end, 2);

% plot the data
subplot(3,2 , 4);
plot(x, y, 'linewidth', 1);
% add labels and title
xlabel('Time (s)');
xlim([0.83 0.89]);
ylim([0 0.6]);
% grid on;
% grid minor;
ylabel('Sensor Output (V)');
% title('Shot 18');



data = readmatrix('./25_8_21_#18_stored_energy.dat');
x2 = data(:, 1);
y2 = data(:, 2);
subplot(3,2 ,3);

%Both data y and y2 should be somewhere directly proportional. However, the time data is messed up a little bit.
% Can you align the curvatures so that they overlap as much as possible?
plot(x2, y2, 'linewidth', 1, 'Color', [0.8500, 0.3250, 0.0980]);
xlim([0.8 0.86]);
ylim([-5 65]);
% grid on;
% grid minor;
xlabel('Time (s)');
ylabel('Stored Energy (J)');
% title('Shot 18');




% Shot 19

opts = detectImportOptions('scope_11.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double');
opts = setvaropts(opts, 'DecimalSeparator', '.');
data = readmatrix('scope_11.csv', opts);
x = data(4:end, 1);
y = data(4:end, 2);

% plot the data
subplot(3,2 , 6);
plot(x, y, 'linewidth', 1);
% add labels and title
xlabel('Time (s)');
xlim([0.83 0.89]);
ylim([0 0.6]);
% grid on;
% grid minor;
ylabel('Sensor Output (V)');
% title('Shot 19');


data = readmatrix('./25_8_21_#19_stored_energy.dat');
x2 = data(:, 1);
y2 = data(:, 2);
subplot(3,2 ,5);

%Both data y and y2 should be somewhere directly proportional. However, the time data is messed up a little bit.
% Can you align the curvatures so that they overlap as much as possible?
plot(x2, y2, 'linewidth', 1, 'Color', [0.8500, 0.3250, 0.0980]);
xlim([0.8 0.86]);
ylim([-5 65]);
% grid on;
% grid minor;
xlabel('Time (s)');
ylabel('Stored Energy (J)');
% title('Shot 19');
% sgtitle('Half Tesla QHS Mode', 'FontSize', 14, 'FontWeight', 'bold');
