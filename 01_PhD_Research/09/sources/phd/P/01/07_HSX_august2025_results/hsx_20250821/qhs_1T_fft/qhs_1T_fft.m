% Load all .csv files into matlab two columns into x and y
% plot individual figures for each file
% save all figures into png files
clear; close all; clc;
files = dir('*.csv');
figure;

% only load files with name scope_ 62, 64, 66
hold on;
grid on;
grid minor
legend show;
for i = 1:length(files)
    if contains(files(i).name, 'scope_62')  || contains(files(i).name, 'scope_64') || contains(files(i).name, 'scope_66')
        % read the data from the csv file, read more decimal places
        opts = detectImportOptions(files(i).name, 'NumHeaderLines', 0);
        opts = setvartype(opts, 'double');
        opts = setvaropts(opts, 'DecimalSeparator', '.');
        data = readmatrix(files(i).name, opts);
        x = data(4:end, 1);
        y = data(4:end, 2);
         %{
        % plot the data
        plot(x, y);
        % add labels and title
        xlabel('Time (s)');
        ylabel('Output Voltage (V)');
        xlim([0.4 1]);
        ylim([0 0.45]);
        title(["One Tesla QHS Mode, Sensor On vs Off"]);
        %}
       
        % x is the time, y is the voltage. This is the time domain data. I would like to perform a fft analysis to the voltage using the time data from x
        fs = 1/(x(10)-x(9)); % Sampling frequency
        n = length(y); % Number of samples
        f = fs*(0:(n/2))/n; % Frequency range
        Y = fft(y); % FFT of the signal
        P = abs(Y/n); % Normalize the FFT
        P = P(1:n/2+1); % Keep only the positive frequencies
        % is P in dB?
        P_db = 20*log10(P);
        % plot the FFT
        plot(f, P);
        % add labels and title
        xlabel('Frequency (Hz)');
        ylabel('Magnitude');
        title(["One Tesla QHS Mode, V_{bias} = 0.4 V"]);
        xlim([23 5500]);
        
        
    end
    % create a new figure
    
    % save the figure as a png file
    
end
% add legend
legend({'Shot 63, V{bias} = 0 V', 'Shot 64', 'Shot 65'}, 'Location', 'Best');
saveas(gcf, ['qhs_1T_1s_onvsoff.png']);
    % close the figure