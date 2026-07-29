% Load all .csv files into matlab two columns into x and y
% plot individual figures for each file
% save all figures into png files
% clear; close all; clc;
% files = dir('*.csv');
% figure;

% % only load files with name scope_ 62, 64, 66
% hold on;
% grid on;
% grid minor
% legend show;
% x = [];
% y = [];
% for i = 1:length(files)
%     if contains(files(i).name, 'scope_66') || contains(files(i).name, 'scope_62')
%         % read the data from the csv file, read more decimal places
%         opts = detectImportOptions(files(i).name, 'NumHeaderLines', 0);
%         opts = setvartype(opts, 'double');
%         opts = setvaropts(opts, 'DecimalSeparator', '.');
%         data = readmatrix(files(i).name, opts);
%         x = data(4:end, 1);
%         y = data(4:end, 2) - (4*10^(-3));
%         % y = y/0.32;
        
%         % plot the data
%         plot(x, y, 'linewidth', 1);
%         % add labels and title
%         % Increase the font size of the axes and bold the font weight
%         set(gca, 'FontSize', 12, 'FontWeight', 'bold');
%         xlabel('Time (s)');
%         ylabel('Output Voltage (V)');
%         xlim([0.4 1]);
%         ylim([0 0.4]);
%         title(["One Tesla QHS Mode, Sensor On vs Off"]);
%         hold on;
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
% legend('Shot 63, V_{bias} = 0 V', 'Shot 65, V_{bias} = 0.4 V');

% % data = load('./hsxMainCoilCurrent_shot65.txt');
% % x2 = data(:, 1);
% % y2 = data(:, 2);
% % yyaxis right


% % %Both data y and y2 should be somewhere directly proportional. However, the time data is messed up a little bit.
% % % Can you align the curvatures so that they overlap as much as possible?
% % plot(x2, y2/max(y2), 'linewidth', 1);
% % ylabel('Normalized Main Coil Current (I/I_{max})');
% % xlim([0 1]);
% % ylim([-0.1 1.1]);
% % legend('Hall Sensor Output Voltage', 'Main Coil Current', 'Location', 'southeast');


clear; close all; clc;
files = dir('*.csv');
figure;

% only load files with name scope_ 62, 64, 66
hold on;
% box on;
ax = gca;
ax.Box = 'on';          % full frame
ax.LineWidth = 1;
ax.FontSize = 11;
ax.TickDir = 'out';     % or 'in' if you prefer
ax.XMinorTick = 'off';
ax.YMinorTick = 'off';
% grid on;
% grid minor
legend show;
x = [];
y = [];
%amplifier has an offset of 4 mV
amp_offset = 4*10^(-3);


for i = 1:length(files)
    % if contains(files(i).name, 'scope_66') || contains(files(i).name, 'scope_72')
    if contains(files(i).name, 'scope_66') 
        % read the data from the csv file, read more decimal places
        opts = detectImportOptions(files(i).name, 'NumHeaderLines', 0);
        opts = setvartype(opts, 'double');
        opts = setvaropts(opts, 'DecimalSeparator', '.');
        data = readmatrix(files(i).name, opts);
        x = data(4:end, 1);
        y = data(4:end, 2) - amp_offset;
        % y = y/0.32;
        
        % plot the data
        % left axis
        %  yyaxis left
        % adjust the linewidth to suitable for publication
        plot(x, y, 'linewidth', 1.5, 'Color', [0.8500, 0.3250, 0.0980]);
        % add labels and title
        % Increase the font size of the axes and bold the font weight
        % set(gca, 'FontSize', 12, 'FontWeight', 'bold');
        xlabel('Time (s)');
        % ylabel('Normalized Output Voltage (V/V_{max})');
        xlim([0.4 1]);
        ylim([0 0.4]);
        ylabel('Output Voltage (V)');
        % title(["Main Coil Current (Reference Sensor)"]);
        hold on;
        %}
        %{
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
        title(["One Tesla QHS Mode FFT, V_{bias} = 0.25 V"]);
        xlim([24 6000]);
        %}
        %{
        
        dt = x(10)-x(9);           % safer than x(10)-x(9)
        fs = 1/dt;
        Fs = 1 / (dt); % Calculate sampling frequency from your time data
        L = length(y);         % Get the number of samples

        Y = fft(y);            % Perform the Fast Fourier Transform

        % Compute the two-sided spectrum P2, then the single-sided spectrum P1.
        P2 = abs(Y/L);
        P1 = P2(1:L/2+1);
        P1(2:end-1) = 2*P1(2:end-1);

        % 3. --- CONVERT TO dB AND CREATE FREQUENCY AXIS ---
        P1_dB = 20*log10(P1);   % Convert the magnitude to decibels (dB)

        % Define the frequency domain f
        f = Fs*(0:(L/2))/L;
        plot(f, P1_dB);
        xlabel('Frequency (Hz)');
        ylabel('Magnitude');
        title(["One Tesla Low Elongation Mode FFT, V_{bias} = 0.4 V"]);
        xlim([0 5000]);
        %}
    end
    % create a new figure
    
    % save the figure as a png file
    
end

for i = 1:length(files)
    % if contains(files(i).name, 'scope_66') || contains(files(i).name, 'scope_72')
    if contains(files(i).name, 'scope_62') 
        % read the data from the csv file, read more decimal places
        opts = detectImportOptions(files(i).name, 'NumHeaderLines', 0);
        opts = setvartype(opts, 'double');
        opts = setvaropts(opts, 'DecimalSeparator', '.');
        data = readmatrix(files(i).name, opts);
        x = data(4:end, 1);
        y = data(4:end, 2) - amp_offset;
        % y = y/0.32;
        
        % plot the data
        % left axis
        %  yyaxis left
        plot(x, y, 'linewidth', 1.5, 'Color', [0, 0.4470, 0.7410]	);
        % add labels and title
        % Increase the font size of the axes and bold the font weight
        % set(gca, 'FontSize', 12, 'FontWeight', 'bold');
        xlabel('Time (s)');
        % ylabel('Normalized Output Voltage (V/V_{max})');
        xlim([0.4 1]);
        ylim([0 0.4]);
        ylabel('Amplified Sensor Output (V)');
        % title(["Main Coil Current (Reference Sensor)"]);
        hold on;
        %}
        %{
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
        title(["One Tesla QHS Mode FFT, V_{bias} = 0.25 V"]);
        xlim([24 6000]);
        %}
        %{
        
        dt = x(10)-x(9);           % safer than x(10)-x(9)
        fs = 1/dt;
        Fs = 1 / (dt); % Calculate sampling frequency from your time data
        L = length(y);         % Get the number of samples

        Y = fft(y);            % Perform the Fast Fourier Transform

        % Compute the two-sided spectrum P2, then the single-sided spectrum P1.
        P2 = abs(Y/L);
        P1 = P2(1:L/2+1);
        P1(2:end-1) = 2*P1(2:end-1);

        % 3. --- CONVERT TO dB AND CREATE FREQUENCY AXIS ---
        P1_dB = 20*log10(P1);   % Convert the magnitude to decibels (dB)

        % Define the frequency domain f
        f = Fs*(0:(L/2))/L;
        plot(f, P1_dB);
        xlabel('Frequency (Hz)');
        ylabel('Magnitude');
        title(["One Tesla Low Elongation Mode FFT, V_{bias} = 0.4 V"]);
        xlim([0 5000]);
        %}
    end
    % create a new figure
    
    % save the figure as a png file
    
end

% legend in top left corner
% change legend to top left corner
legend('Shot 65, V_{bias} = 0.4 V', 'Shot 63, V_{bias} = 0 V', 'Location', 'northwest');
% title('1 Tesla QHS Mode, Sensor On vs Off');
data = load('./hsxMainCoilCurrent_shot65.txt');
x2 = data(:, 1);
y2 = data(:, 2);
% yyaxis right


% %Both data y and y2 should be somewhere directly proportional. However, the time data is messed up a little bit.
% % Can you align the curvatures so that they overlap as much as possible?
% plot(x2, y2/max(y2), 'linewidth', 1);
% ylabel('Normalized Main Coil Current (I/I_{max})');
% xlim([0.2 1]);
% ylim([-0.1 1.1]);
% legend('Main Coil Current', 'Location', 'southeast');