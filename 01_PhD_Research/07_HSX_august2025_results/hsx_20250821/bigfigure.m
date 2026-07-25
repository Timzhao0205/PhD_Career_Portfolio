clear; close all; clc;

% ==========================================
% MASTER FONT SETTINGS
% ==========================================
tickFontSize = 11;              % Size of the numbers on the axes
labelFontSize = 13;             % Increased by 1 (was 11)
panelFontSize = 13;             % Match the label font size

% 1. Create the figure with exact IEEE dimensions (Width: 3.46", Height: 2.58")
fig = figure('Color', 'w', 'Units', 'inches', 'Position', [1, 1, 3.46*1.5, 2.58*1.5]); % Scale up by 1.5 for better visibility during editing

% 2. Use tiledlayout for tight academic spacing
t = tiledlayout(3, 2, 'TileSpacing', 'compact', 'Padding', 'compact');

% ==========================================
% ROW 1: Optimal Plasma (Shot 21)
% ==========================================
% --- Left: Stored Energy ---
nexttile;
data_e21 = readmatrix('./25_8_21_#21_stored_energy.dat');
plot(data_e21(:, 1), data_e21(:, 2), 'linewidth', 1.5, 'Color', 'k'); % Pure black
hold on; box on;
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1.2, 'TickDir', 'in', 'XTickLabel', []);
xlim([0.8 0.86]); ylim([-5 65]);
% Panel label inside frame (top-left)
text(0.05, 0.88, '(a)', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold');

% --- Right: Sensor Output ---
nexttile;
opts = detectImportOptions('scope_13.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_s21 = readmatrix('scope_13.csv', opts);
plot(data_s21(4:end, 1), data_s21(4:end, 2), 'linewidth', 1.5, 'Color', [0, 0, 1]); % Pure blue
hold on; box on;
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1.2, 'TickDir', 'in', 'XTickLabel', []);
xlim([0.83 0.89]); ylim([0 0.6]);
% Panel label inside frame (top-right)
text(0.95, 0.88, '(a'')', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold', 'HorizontalAlignment', 'right');


% ==========================================
% ROW 2: Delayed Breakdown (Shot 18) - APPLIES Y-LABELS
% ==========================================
% --- Left: Stored Energy ---
nexttile;
data_e18 = readmatrix('./25_8_21_#18_stored_energy.dat');
plot(data_e18(:, 1), data_e18(:, 2), 'linewidth', 1.5, 'Color', 'k'); % Pure black
hold on; box on;
ylabel('Stored Energy (J)', 'FontSize', labelFontSize, 'FontWeight', 'bold'); 
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1.2, 'TickDir', 'in', 'XTickLabel', []);
xlim([0.8 0.86]); ylim([-5 65]);
% Panel label inside frame (top-left)
text(0.05, 0.88, '(b)', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold');

% --- Right: Sensor Output ---
nexttile;
opts = detectImportOptions('scope_10.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_s18 = readmatrix('scope_10.csv', opts);
plot(data_s18(4:end, 1), data_s18(4:end, 2), 'linewidth', 1.5, 'Color', [0, 0, 1]); % Pure blue
hold on; box on;
ylabel('Amplified Sensor Output,{\it V_{out}} (V)', 'FontSize', labelFontSize, 'FontWeight', 'bold'); 
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1.2, 'TickDir', 'in', 'XTickLabel', []);
xlim([0.83 0.89]); ylim([0 0.6]);
% Panel label inside frame (top-right)
text(0.95, 0.88, '(b'')', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold', 'HorizontalAlignment', 'right');


% ==========================================
% ROW 3: Aborted Breakdown (Shot 19) - APPLIES X-LABELS
% ==========================================
% --- Left: Stored Energy ---
nexttile;
data_e19 = readmatrix('./25_8_21_#19_stored_energy.dat');
plot(data_e19(:, 1), data_e19(:, 2), 'linewidth', 1.5, 'Color', 'k'); % Pure black
hold on; box on;
xlabel('Time (s)', 'FontSize', labelFontSize, 'FontWeight', 'bold'); 
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1.2, 'TickDir', 'in'); 
xlim([0.8 0.86]); ylim([-5 65]);
% Panel label inside frame (top-left)
text(0.05, 0.88, '(c)', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold');

% --- Right: Sensor Output ---
nexttile;
opts = detectImportOptions('scope_11.csv', 'NumHeaderLines', 0);
opts = setvartype(opts, 'double'); opts = setvaropts(opts, 'DecimalSeparator', '.');
data_s19 = readmatrix('scope_11.csv', opts);
plot(data_s19(4:end, 1), data_s19(4:end, 2), 'linewidth', 1.5, 'Color', [0, 0, 1]); % Pure blue
hold on; box on;
xlabel('Time (s)', 'FontSize', labelFontSize, 'FontWeight', 'bold'); 
set(gca, 'FontSize', tickFontSize, 'LineWidth', 1.2, 'TickDir', 'in');
xlim([0.83 0.89]); ylim([0 0.6]);
% Panel label inside frame (top-right)
text(0.95, 0.88, '(c'')', 'Units', 'normalized', 'FontSize', panelFontSize, 'FontWeight', 'bold', 'HorizontalAlignment', 'right');

% ==========================================
% EXPORT
% ==========================================
% Lock export size to exactly match the screen
set(fig, 'PaperPositionMode', 'auto');

% Export as high-res PNG
exportgraphics(fig, 'Fig4_PlasmaDynamics_Final.png', 'Resolution', 300);