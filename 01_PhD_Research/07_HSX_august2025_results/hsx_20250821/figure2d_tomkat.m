clear; close all; clc;

% ==========================================
% MASTER FONT & LAYOUT SETTINGS
% ==========================================
tickFontSize = 10;              % Size of the numbers on the axes
labelFontSize = 14;             % Size of 'Time', 'Amplified Sensor Output', etc.

amp_offset = 4*10^(-3);         % Amplifier offset to subtract from data

% --- Legend Positioning Controls ---
legendXOffset = 0.06; % Inches from the inner left edge of the plot frame
legendYOffset = 0.06; % Inches from the inner top edge of the plot frame

% ==========================================
% EXACT SIZING CALCULATIONS (INCHES)
% ==========================================
% Define exact plot dimensions requested
plotWidth = 3.36;  % Exact width of the plot area (not including margins)
plotHeight = 3;

% Define margins around the plots to fit labels and titles
leftMargin = 0.65;   % Space for y-labels
rightMargin = 0.1;  % Right edge buffer
bottomMargin = 0.5; % Space for bottom x-label
topMargin = 0.1;    % Space for top margin (reduced since no panel letter)

% Calculate total figure size required to house the single plot
figWidth = leftMargin + plotWidth + rightMargin;
figHeight = bottomMargin + plotHeight + topMargin;

% 1. Create the figure with exact calculated dimensions
fig = figure('Color', 'w', 'Units', 'inches', 'Position', [1, 1, figWidth, figHeight]);


% ==========================================
% MAIN PANEL: Biased vs Unbiased
% ==========================================
% 2. Manually position the axes to guarantee exact size
ax1_bottom = bottomMargin;
ax1 = axes('Units', 'inches', 'Position', [leftMargin, ax1_bottom, plotWidth, plotHeight]);
hold on; box on;

% Load and plot scope_66.csv (Biased) - Blue
opts = detectImportOptions('scope_66.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_66 = readmatrix('scope_66.csv', opts);
plot(data_66(4:end, 1), data_66(4:end, 2) - amp_offset, 'linewidth', 1.5, 'Color', [0,0,1]);

% Load and plot scope_62.csv (Unbiased) - Black
opts = detectImportOptions('scope_62.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_62 = readmatrix('scope_62.csv', opts);
plot(data_62(4:end, 1), data_62(4:end, 2) - amp_offset, 'linewidth', 1.5, 'Color', 'k');

% Format axes (Titles now Bold)
xlabel('Time (s)', 'FontSize', labelFontSize, 'FontWeight', 'bold');
ylabel('Amplified Sensor Output, {\it V_{out}} (V)', 'FontSize', labelFontSize, 'FontWeight', 'bold'); 
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1, 'TickDir', 'in', ...
    'XMinorTick', 'off', 'YMinorTick', 'off');
xlim([0.4 1]); ylim([0 0.4]);

% Custom Legend Positioning
lgd1 = legend('Powered Sensor, V_{bias} = 0.4 V', 'Unpowered Sensor, V_{bias} = 0 V');
lgd1.Units = 'inches';
% Calculate exact Y position: Top of axis - height of legend - desired offset
ax1Top = ax1_bottom + plotHeight;
lgd1.Position(1) = leftMargin + legendXOffset;
lgd1.Position(2) = ax1Top - lgd1.Position(4) - legendYOffset;


% ==========================================
% EXPORT
% ==========================================
% Lock the export size to exactly match the screen
set(fig, 'PaperPositionMode', 'auto');
exportgraphics(fig, 'Fig3_SensorVerification_Single.png', 'Resolution', 300);