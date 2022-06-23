#define OPTION_LENGTH 50

struct menuOptionDetails
{
	char descriptionOfOptions[150];
	char saveOption[OPTION_LENGTH];
	char displayOption[OPTION_LENGTH];
	char searchOption[OPTION_LENGTH];
	char updateOption[OPTION_LENGTH];
	char deleteOption[OPTION_LENGTH];
	char exitOption[OPTION_LENGTH];
	char optionNumbers[OPTION_LENGTH]
}
int userShowMenu()
{
	struct menuOptionDetails menuDetails;
	printf("Write description before options list: ");
	scanf("%s", menuDetails.descriptionOfOptions);
	printf("How do you want to print save option: ");
	scanf("%s", menuDetails.saveOption);
	printf("How do you want to print display option: ");
	scanf("%s", menuDetails.displayOption);
	printf("How do you want to print search option: ");
	scanf("%s", menuDetails.searchOption);
	printf("How do you want to print update option: ");
	scanf("%s", menuDetails.updateOption);
	printf("How do you want to print delete option: ");
	scanf("%s", menuDetails.deleteOption);
	printf("How do you want to print exit option: ");
	scanf("%s", menuDetails.exitOption);
	printf("How do you want to show numbers of options(1, 2, 3, 4, 5 or 6): ");
	scanf("%s", menuDetails.optionNumbers);
}