clear; close all; clc;

% ==========================================
% MASTER FONT & LAYOUT SETTINGS
% ==========================================
tickFontSize = 10;              % Size of the numbers on the axes
labelFontSize = 12;             % Size of 'Time', 'Amplified Sensor Output', etc. (Increased to 12)
panelFontSize = 11;             % '(a)', '(b)' labels kept at 11, or change to labelFontSize if you want them to match

amp_offset = 4*10^(-3);         % Amplifier offset to subtract from data

% --- Legend Positioning Controls ---
legendXOffset = 0.06; % Inches from the inner left edge of the plot frame
legendYOffset = 0.06; % Inches from the inner top edge of the plot frame

% ==========================================
% EXACT SIZING CALCULATIONS (INCHES)
% ==========================================
% Define exact plot dimensions requested
plotWidth = 3.46;
plotHeight = 2.58;

% Define margins around the plots to fit labels and titles
leftMargin = 0.65;   % Space for y-labels
rightMargin = 0.15;  % Right edge buffer
bottomMargin = 0.55; % Space for bottom x-label
midSpacing = 0.65;   % Space between plots (for top x-label)
topMargin = 0.30;    % Space for top panel label '(a)'

% Calculate total figure size required to house the exact plot dimensions
figWidth = leftMargin + plotWidth + rightMargin;
figHeight = bottomMargin + plotHeight + midSpacing + plotHeight + topMargin;

% 1. Create the figure with exact calculated dimensions
fig = figure('Color', 'w', 'Units', 'inches', 'Position', [1, 1, figWidth, figHeight]);


% ==========================================
% TOP PANEL (a): Biased vs Unbiased
% ==========================================
% 2. Manually position the top axes to guarantee exact size
ax1_bottom = bottomMargin + plotHeight + midSpacing;
ax1 = axes('Units', 'inches', 'Position', [leftMargin, ax1_bottom, plotWidth, plotHeight]);
hold on; box on;

% Load and plot scope_66.csv (Biased) - Black
opts = detectImportOptions('scope_66.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_66 = readmatrix('scope_66.csv', opts);
plot(data_66(4:end, 1), data_66(4:end, 2) - amp_offset, 'linewidth', 1.5, 'Color', 'k');

% Load and plot scope_62.csv (Unbiased) - Cooler Blue (#2F2EF4)
opts = detectImportOptions('scope_62.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_62 = readmatrix('scope_62.csv', opts);
plot(data_62(4:end, 1), data_62(4:end, 2) - amp_offset, 'linewidth', 1.5, 'Color', [0,0,1]);

% Format axes (Titles now Bold)
xlabel('Time (s)', 'FontSize', labelFontSize, 'FontWeight', 'bold');
ylabel('Amplified Sensor Output,{\it V_{out}} (V)', 'FontSize', labelFontSize, 'FontWeight', 'bold'); 
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1, 'TickDir', 'in', ...
    'XMinorTick', 'off', 'YMinorTick', 'off');
xlim([0.4 1]); ylim([0 0.4]);

% Custom Legend Positioning
lgd1 = legend('Biased Sensor, V_{bias} = 0.4 V', 'Unbiased Sensor, V_{bias} = 0 V');
lgd1.Units = 'inches';
% Calculate exact Y position: Top of axis - height of legend - desired offset
ax1Top = ax1_bottom + plotHeight;
lgd1.Position(1) = leftMargin + legendXOffset;
lgd1.Position(2) = ax1Top - lgd1.Position(4) - legendYOffset;

% Panel Label (Outside frame: Top-Left)
text(-0.15, 1.08, '(a)', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold', ...
    'HorizontalAlignment', 'left', 'Clipping', 'off');


% ==========================================
% BOTTOM PANEL (b): Plasma vs Coil-Only
% ==========================================
% 3. Manually position the bottom axes
ax2 = axes('Units', 'inches', 'Position', [leftMargin, bottomMargin, plotWidth, plotHeight]);
hold on; box on;

% Plot scope_66.csv again (Plasma Discharge) - Black
plot(data_66(4:end, 1), data_66(4:end, 2) - amp_offset, 'linewidth', 1.5, 'Color', 'k');

% Load and plot scope_72.csv (Coil-Only) - Cooler Blue (#2F2EF4)
opts = detectImportOptions('scope_72.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_72 = readmatrix('scope_72.csv', opts);
plot(data_72(4:end, 1), data_72(4:end, 2) - amp_offset, 'linewidth', 1.5, 'Color', [0,0,1]);

% Format axes (Titles now Bold)
xlabel('Time (s)', 'FontSize', labelFontSize, 'FontWeight', 'bold');
ylabel('Amplified Sensor Output,{\it V_{out}} (V)', 'FontSize', labelFontSize, 'FontWeight', 'bold'); 
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1, 'TickDir', 'in', ...
    'XMinorTick', 'off', 'YMinorTick', 'off');
xlim([0.4 1]); ylim([0 0.4]);

% Custom Legend Positioning
lgd2 = legend('Plasma Discharge', 'Coil-Only Shot');
lgd2.Units = 'inches';
% Calculate exact Y position: Top of axis - height of legend - desired offset
ax2Top = bottomMargin + plotHeight;
lgd2.Position(1) = leftMargin + legendXOffset;
lgd2.Position(2) = ax2Top - lgd2.Position(4) - legendYOffset;

% Panel Label (Outside frame: Top-Left)
text(-0.15, 1.08, '(b)', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold', ...
    'HorizontalAlignment', 'left', 'Clipping', 'off');


% ==========================================
% EXPORT
% ==========================================
% Lock the export size to exactly match the screen
set(fig, 'PaperPositionMode', 'auto');
exportgraphics(fig, 'Fig3_SensorVerification_Combined.png', 'Resolution', 300);