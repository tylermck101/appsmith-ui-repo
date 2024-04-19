export default {
    async setColor() {
				let colors = await ColorSchemeByMood.run(UserMood.data);
        storeValue('primaryColor', colors.headerColor);
        storeValue('backgroundColor', colors.backgroundColor);
			  storeValue('textColor', colors.textColor);
    }
}