package com.example.final_proyect;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

public class VintageCars extends AppCompatActivity {
    private Button btn_volverAtras3;
    private ImageButton imageBtnCasa3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_vintage_cars);
        btn_volverAtras3 = (Button)findViewById(R.id.btn_volverAtras3);
        imageBtnCasa3 = (ImageButton)findViewById(R.id.imageBtnCasa3);
        volverAtras3();
        Casa();
    }
    public void volverAtras3(){
        btn_volverAtras3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(VintageCars.this,Catalogo.class);
                startActivity(ant);
            }
        });


    }
    public void Casa(){
        imageBtnCasa3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(VintageCars.this,MainActivity.class);
                startActivity(ant);
            }
        });


    }
    public void imagebtnUniversalACSixSedan(View view) {
        Toast.makeText(this, "¡Universal AC Six Sedan!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtn53FordCustomline(View view) {
        Toast.makeText(this, "¡53 Ford Customline!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnCorvetteZL1(View view) {
        Toast.makeText(this, "¡Corvette ZL1!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnChevroletChevelleSS(View view) {
        Toast.makeText(this, "¡Chevrolet Chevelle SS!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnC1corvete(View view) {
        Toast.makeText(this, "¡C1 corvete!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnCandyRed57ChevyBelAir(View view) {
        Toast.makeText(this, "¡CandyRed'57ChevyBelAir!", Toast.LENGTH_SHORT).show();
    }
}