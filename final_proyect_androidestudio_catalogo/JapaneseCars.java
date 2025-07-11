package com.example.final_proyect;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

public class JapaneseCars extends AppCompatActivity {
    private Button  btn_volverAtras1;
    private ImageButton imageBtnCasa1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_japanese_cars);
        btn_volverAtras1 =(Button) findViewById(R.id.btn_volverAtras1);
        volverAtras1();
        imageBtnCasa1 =(ImageButton) findViewById(R.id.imageBtnCasa1);
        Casa();

        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayShowTitleEnabled(false);
        }

    }
    public void volverAtras1(){
        btn_volverAtras1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(JapaneseCars.this,Catalogo.class);
                startActivity(ant);
            }
        });


    }
    public void Casa(){
        imageBtnCasa1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(JapaneseCars.this,MainActivity.class);
                startActivity(ant);
            }
        });


    }
    public void imagebtnNissan240SX(View view) {
        Toast.makeText(this, "¡Nissan 240SX!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnJzx100(View view) {
        Toast.makeText(this, "¡Toyota Chaser V JZX100!", Toast.LENGTH_SHORT).show();
    }

    public void imagebtnNissanskyline(View view) {
        Toast.makeText(this, "¡Nissan Skyline", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnRx7(View view) {
        Toast.makeText(this, "¡Mazda RX7!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnNissanSilviaS15(View view) {
        Toast.makeText(this, "¡Nissan Silvia S15!", Toast.LENGTH_SHORT).show();
    }
    public void imagebtnToyotaSupra(View view) {
        Toast.makeText(this, "¡Toyota Supra!", Toast.LENGTH_SHORT).show();
    }




}