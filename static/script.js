function openTab(tabName) {
  // Declare all variables
  let i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  document.getElementById(tabName.toLowerCase() + '_tab').className += " active";

  console.log(`initialize tab ${tabName}`);
  // call initialization code of the module
  switch (tabName) {
    case 'Dashboard': dashboardInit(); break;
    case 'Mutieren': mutateInit(); break;
    case 'Vorerfassung': preEnterInit(); break;
    case 'Konfiguration': settingsInit(); break;
    default:
  }
}

window.onload = function() {
    // Open the dashboard tab, when application has finished loading
    console.log('window.onlad entered!');
    openTab('Dashboard');
}