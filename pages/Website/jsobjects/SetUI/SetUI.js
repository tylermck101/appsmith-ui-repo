export default function applyColorScheme(colors) {
	// Assuming `colors` is the API response containing the color scheme
	appsmith.store.update({
		headerColor: colors.headerColor,
		textColor: colors.textColor,
		backgroundColor: colors.backgroundColor
	});
}