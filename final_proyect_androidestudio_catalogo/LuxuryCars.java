package com.example.final_proyect;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

public class LuxuryCars extends AppCompatActivity {
    private Button btn_volverAtras4;
    private ImageButton imageBtnCasa4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_luxury_cars);
        btn_volverAtras4 = (Button)findViewById(R.id.btn_volverAtras4);
        imageBtnCasa4 = (ImageButton)findViewById(R.id.imageBtnCasa4);
        volverAtras4();
        Casa();
    }
    public void volverAtras4(){
        btn_volverAtras4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(LuxuryCars.this,Catalogo.class);
                startActivity(ant);
            }
        });


    }
    public void Casa(){
        imageBtnCasa4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(LuxuryCars.this,MainActivity.class);
                startActivity(ant);
            }
        });


    }
    public void imagebtnFordF150(View view) {
        Toast.makeText(this, "¡Ford F-150!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnAudiRs5(View view) {
        Toast.makeText(this, "¡Audi Rs5!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnBMWX6M(View view) {
        Toast.makeText(this, "¡BMW X6 M!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnFerrariSF90Stradale(View view) {
        Toast.makeText(this, "¡Ferrari SF90 Stradale!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnG63AMG(View view) {
        Toast.makeText(this, "¡G63 AMG!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnMcLaren720S(View view) {
        Toast.makeText(this, "¡McLaren 720S!", Toast.LENGTH_SHORT).show();
    }

}