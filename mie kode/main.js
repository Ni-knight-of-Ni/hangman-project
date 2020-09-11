var firebaseConfig = {
  apiKey: "AIzaSyDGvIh0j65Rm839wsFdVM9ePBhoqz8U2Os",
  authDomain: "snake-f2681.firebaseapp.com",
  databaseURL: "https://snake-f2681.firebaseio.com",
  projectId: "snake-f2681",
  storageBucket: "snake-f2681.appspot.com",
  messagingSenderId: "585028498730",
  appId: "1:585028498730:web:2905fc1d05d2821b641a53"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Reference tempData collection
var tempDataRef = firebase.database().ref('tempData');


var d = new Date(),
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    day = days[d.getDay()],
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    month = months[d.getMonth()],
    date = d.getDate(),
    suf = ['th','st','nd','rd'],
    v = date%100,
    date = date+(suf[(v-20)%10]||suf[v]||suf[0]),
    hours = d.getHours(),
    minutes = d.getMinutes(),
    noon = '';
// Display hours in 12-hour format, and set am/pm
if (hours==12) {
  noon = 'pm';
} else if (hours>12) {
  hours = hours-12;
  noon = 'pm';
} else {
  noon = 'am';
};
// Add '0' to minutes if less than 10
if(minutes<10) {
  minutes ='0'+minutes;
};
// Output the Timestamp
var timestamp = day+' '+month+' '+date+', '+hours+':'+minutes+' '+noon;

// Listen for form submit
document.getElementById('contactForm1').addEventListener('submit', submitForm1);

// Submit form
function submitForm1(e){
  e.preventDefault();
  // Save message
  saveMessage("up", timestamp);
  // Clear form
}
// Listen for form submit
document.getElementById('contactForm2').addEventListener('submit', submitForm2);

// Submit form
function submitForm2(e){
  e.preventDefault();
  // Save message
  saveMessage("left", timestamp);
  // Clear form

}
// Listen for form submit
document.getElementById('contactForm3').addEventListener('submit', submitForm3);

// Submit form
function submitForm3(e){
  e.preventDefault();
  // Save message
  saveMessage("right", timestamp);
  // Clear form
}
// Listen for form submit
document.getElementById('contactForm4').addEventListener('submit', submitForm4);

// Submit form
function submitForm4(e){
  e.preventDefault();
  // Save message
  saveMessage("down", timestamp);
  // Clear form

}
// Save message to firebase
function saveMessage(et, to){
  var newMessageRef = tempDataRef.push();
  newMessageRef.set({
    Start:et,
    Time:to
  });
}
