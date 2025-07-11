package com.example.final_proyect;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

public class FormulaCars extends AppCompatActivity {
    private Button btn_volverAtras2;
    private ImageButton imageBtnCasa2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_formula_cars);
        btn_volverAtras2 = (Button)findViewById(R.id.btn_volverAtras2);
        imageBtnCasa2 = (ImageButton)findViewById(R.id.imageBtnCasa2);
        volverAtras2();
        Casa();

    }
    public void volverAtras2(){
        btn_volverAtras2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(FormulaCars.this,Catalogo.class);
                startActivity(ant);
            }
        });


    }
    public void Casa(){
        imageBtnCasa2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(FormulaCars.this,MainActivity.class);
                startActivity(ant);
            }
        });


    }
    public void imagebtnAlpineA523(View view) {
        // Muestra un mensaje con Toast
        Toast.makeText(this, "¡Alpine A523!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnF1Fw45(View view) {
        // Muestra un mensaje con Toast
        Toast.makeText(this, "¡Williams FW45!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnMercedesF144(View view) {
        // Muestra un mensaje con Toast
        Toast.makeText(this, "¡Mercedes F1-44!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnRB19MaxVerstappen(View view) {
        // Muestra un mensaje con Toast
        Toast.makeText(this, "¡RB19!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnFerrariF175(View view) {
        // Muestra un mensaje con Toast
        Toast.makeText(this, "¡Ferrari F1-75!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnRB16B(View view) {
        // Muestra un mensaje con Toast
        Toast.makeText(this, "¡RB16B!", Toast.LENGTH_SHORT).show();
    }


}