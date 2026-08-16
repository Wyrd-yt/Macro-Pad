#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <SPI.h>
#include <Keyboard.h>
#include <ArduinoJson.h>

// ======================
// TFT ST7735
// ======================
#define TFT_CS   17
#define TFT_DC   16
#define TFT_RST  20
#define TFT_BL   21

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);


// ======================
// Switches
// ======================
const byte switches[8] = {0,1,2,3,4,5,6,7};


// ======================
// Joystick
// ======================
const int joyX = 28;
const int joyY = 27;
const int joySW = 22;


// ======================
// Potentiomètre
// ======================
const int pot = 26;

int currentPos = 0;

bool presetSelected = false;

bool nbPresetSelected[5] = 
  {
    false,
    false,
    false,
    false,
    false
  };

String config[5][11];

String namePreset[5];

int pAncient;

bool loaded = false;
bool mainLoaded = false;


//fonction de refresh l'écran au menu principal
void refreshMain() {

  //efface l'écran
  tft.fillScreen(ST77XX_BLACK);

  tft.setTextSize(2);
  tft.setTextColor(ST77XX_WHITE);

  //affiche MACROPAD
  tft.setCursor(15,5);
  tft.print("MACROPAD");

  //affiche le curseur de selection
  tft.setTextSize(1);
  tft.setCursor(5,45+(currentPos*20));
  tft.print(">");

  //afficher le carré de selection
  int16_t x1, y1;
  uint16_t w, h;

  tft.getTextBounds(namePreset[currentPos], 0, 0, &x1, &y1, &w, &h);

  tft.fillRect(13,45+(currentPos*20)-2, w+2, h+3, ST77XX_WHITE);  //(x, y, longueur, largeur, couleur)


  //affiche les presets
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(1);

  for(int i = 0; i < 5; i++) {
    //si le c'est le preset selectionner on l'écrit en noir
    if (i == currentPos){
      tft.setTextColor(ST77XX_BLACK);
      tft.setCursor(15,45+(i*20));  //U0 + nr suite arithmétique avec U0=45 et r=20
      tft.print(namePreset[i]);
    }
    //sinon on écrit les autres en blanc
    else {
      tft.setTextColor(ST77XX_WHITE);
      tft.setCursor(15,45+(i*20));  //U0 + nr suite arithmétique avec U0=45 et r=20
      tft.print(namePreset[i]);
    }
  }

}

//fonction pour refresh l'écran au presets
void refreshPreset(int currentPos) {

  //efface l'écran
  tft.fillScreen(ST77XX_BLACK);

  //affiche le nom de preset selectionné en grand au milieu de l'écran
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(2);

  int16_t x1, y1;
  uint16_t w1, h1;

  tft.getTextBounds(namePreset[currentPos], 0, 0, &x1, &y1, &w1, &h1);

  tft.setCursor((tft.width() - w1) / 2, (tft.height() - h1) / 2);
  tft.print(namePreset[currentPos]);
  
  //affiche le rectangle de selection sur la croix
  tft.setTextSize(1); //pour qu'il mesure la taille de "X" en taille 1 et pas 2
  int16_t x2, y2;
  uint16_t w2, h2;

  tft.getTextBounds("X", 0, 0, &x2, &y2, &w2, &h2);

  tft.fillRect(8,13, w2+3, h2+3, ST77XX_WHITE);  //(x, y, longueur, largeur, couleur)

  //affiche la croix
  tft.setTextColor(ST77XX_BLACK);
  tft.setCursor(10,15);
  tft.print("X");

}

void loading() {

  //efface l'écran
  tft.fillScreen(ST77XX_BLACK);

  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(1);

  int16_t x1, y1;
  uint16_t w1, h1;

  tft.getTextBounds("LOADING", 0, 0, &x1, &y1, &w1, &h1);

  tft.setCursor((tft.width() - w1) / 2, (tft.height() - h1) / 2);
  tft.print("LOADING");
  delay(500);

  tft.setCursor((tft.width() - w1) / 2, (tft.height() - h1) / 2);
  tft.print("LOADING.");
  delay(500);

  tft.setCursor((tft.width() - w1) / 2, (tft.height() - h1) / 2);
  tft.print("LOADING..");
  delay(500);

  tft.setCursor((tft.width() - w1) / 2, (tft.height() - h1) / 2);
  tft.print("LOADING...");
  delay(500);
  
}


void press(String x) {
  if (x == "1") {
    Keyboard.press(KEY_LEFT_CTRL);
  }

  else if (x == "2") {
    Keyboard.press(KEY_LEFT_SHIFT);
  }

  else if (x == "3") {
    Keyboard.press(KEY_LEFT_ALT);
  }

  else if (x == "4") {
    Keyboard.press(KEY_LEFT_GUI);
  }

  else if (x == "5") {
    Keyboard.press(KEY_TAB);
  }

  else if (x == "6") {
    Keyboard.press(KEY_CAPS_LOCK);
  }

  else if (x == "7") {
    Keyboard.press(' ');
  }

  else if (x == "8") {
    Keyboard.press(KEY_BACKSPACE);
  }

  else if (x == "9") {
    Keyboard.press(KEY_RETURN);
  }

  // RANGEE DU DESSUS
  // La conversion se fait ici car les nombres sont occupés par les codes comme CTRL. On ne peut donc pas remplacé les caracteres de la rangée du haut par les chiffres dans le json
  else if (x == "&") {
    Keyboard.press('1');
  }

  else if (x == "é") {
    Keyboard.press('2');
  }

  else if (x == "\"") {
    Keyboard.press('3');
  }

  else if (x == "'") {
    Keyboard.press('4');
  }

  else if (x == "(") {
    Keyboard.press('5');
  }

  else if (x == "-") {
    Keyboard.press('6');
  }

  else if (x == "è") {
    Keyboard.press('7');
  }
  
  else if (x == "_") {
    Keyboard.press('8');
  }

  else if (x == "ç") {
    Keyboard.press('9');
  }

  else if (x == "à") {
    Keyboard.press('0');
  }

  else if (x == ")") {
    Keyboard.press('-');
  }

  else {
    Keyboard.press(x[0]);
  }
}


void setup() {

  Serial.begin(115200);

  //démarrer les fonctionnalités pour simuler les raccourcis clavier
  Keyboard.begin();


  // ---------
  // Backlight
  // ---------
  pinMode(TFT_BL, OUTPUT);
  digitalWrite(TFT_BL, HIGH);


  // ---------
  // Switches
  // ---------
  for(int i = 0; i < 8; i++) {
    pinMode(switches[i], INPUT_PULLUP);
  }


  // Joystick bouton
  pinMode(joySW, INPUT_PULLUP);



  // ---------
  // TFT
  // ---------
  tft.initR(INITR_BLACKTAB);
  tft.setRotation(0);

  pAncient = analogRead(pot);

  delay(500);
}



void loop() {

  int pNew = analogRead(pot);

  if (Serial.available())
  {
    String message = Serial.readStringUntil('\n');
    JsonDocument presets;

    deserializeJson(presets, message);
    
    for (int i = 0; i < 5; i++) {
      String name = "preset" + String(i+1);
      namePreset[i] = presets[name][0].as<String>();
      for (int j = 0; j < 11; j++){
        config[i][j] = presets[name][j].as<String>();
      }
    }

    loaded = true;

  }

  if (loaded == false && mainLoaded == false) {
    loading();
  }

  if (loaded == true && mainLoaded == false) {
    tft.fillScreen(ST77XX_BLACK);
    refreshMain();
    mainLoaded = true;
  }

  Serial.println("PICO OK");

  // Lecture capteurs

  int x = analogRead(joyX);
  int y = analogRead(joyY);

  //si le joystick descends
  if(x < 500 && currentPos < 4 && presetSelected == false) {
    currentPos++;
    refreshMain();
    delay(100);
  }

  //si le joystick monte
  if(x > 600 && currentPos > 0 && presetSelected == false) {
    currentPos--;
    refreshMain();
    delay(100);
  }

  //si le bouton du joystick est pressé et que le menu main est ouvert
  if (digitalRead(joySW) == LOW && presetSelected == false) {
    if (namePreset[currentPos] != "Aucun") {
      refreshPreset(currentPos);
      delay(200);
      nbPresetSelected[currentPos] = true;
      presetSelected = true;
    }
  }

  //si le bouton du joystick est pressé et qu'un preset est selectionné
  if (digitalRead(joySW) == LOW && presetSelected == true){
    refreshMain();
    delay(200);
    nbPresetSelected[currentPos] = false;
    presetSelected = false;
  }



  //si le 1er est pressé (le premier en partant du haut gauche)
  if (digitalRead(switches[3]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][1].substring(0, 1));
        press(config[i][1].substring(1, 2));
        press(config[i][1].substring(2, 3));
        press(config[i][1].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 2e
  if (digitalRead(switches[2]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][2].substring(0, 1));
        press(config[i][2].substring(1, 2));
        press(config[i][2].substring(2, 3));
        press(config[i][2].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 3e
  if (digitalRead(switches[1]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][3].substring(0, 1));
        press(config[i][3].substring(1, 2));
        press(config[i][3].substring(2, 3));
        press(config[i][3].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 4e
  if (digitalRead(switches[0]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][4].substring(0, 1));
        press(config[i][4].substring(1, 2));
        press(config[i][4].substring(2, 3));
        press(config[i][4].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 5e
  if (digitalRead(switches[7]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][5].substring(0, 1));
        press(config[i][5].substring(1, 2));
        press(config[i][5].substring(2, 3));
        press(config[i][5].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 6e
  if (digitalRead(switches[6]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][6].substring(0, 1));
        press(config[i][6].substring(1, 2));
        press(config[i][6].substring(2, 3));
        press(config[i][6].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 7e
  if (digitalRead(switches[5]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][7].substring(0, 1));
        press(config[i][7].substring(1, 2));
        press(config[i][7].substring(2, 3));
        press(config[i][7].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 8e
  if (digitalRead(switches[4]) == LOW) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {
        press(config[i][8].substring(0, 1));
        press(config[i][8].substring(1, 2));
        press(config[i][8].substring(2, 3));
        press(config[i][8].substring(3, 4));
        delay(20);
        Keyboard.releaseAll();
      }
    }
  }

  // 10 niveaux pour le potentiometre, le premier commence a 023 et le dernier finit a 1023. A chaque palier de +100, le niveau augmente de 1 et invesement à chaque palier de -100.
  // potentiometre vers la droite donc si la valeur du potentiometre augmente
  if (abs(pAncient - pNew) > 100) {
    for (int i = 0; i < 5; i++) {
      if (nbPresetSelected[i] == true) {

        // potentiometre vers la droite donc si la valeur du potentiometre diminue (car c'est inversé)
        if (pAncient > pNew) {
          press(config[i][9].substring(0, 1));
          press(config[i][9].substring(1, 2));
          press(config[i][9].substring(2, 3));
          press(config[i][9].substring(3, 4));
          delay(20);
          Keyboard.releaseAll();
        }

        // potentiometre vers la gauche donc si la valeur du potentiometre diminue
        else {
          press(config[i][10].substring(0, 1));
          press(config[i][10].substring(1, 2));
          press(config[i][10].substring(2, 3));
          press(config[i][10].substring(3, 4));
          delay(20);
          Keyboard.releaseAll();
        }
        pAncient = pNew;

      }
    }
  }

  

  delay(100);

}



