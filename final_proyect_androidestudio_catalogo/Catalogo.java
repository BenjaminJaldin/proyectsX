package com.example.final_proyect;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Catalogo extends AppCompatActivity {
    private Button btn_volverAtras;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalogo);
        btn_volverAtras = (Button)findViewById(R.id.btn_volverAtras);
        volverAtras();
    }
    public void sgtJapaneseCars (View v){
        Intent sig = new  Intent(this,JapaneseCars.class);
        startActivity(sig);
    }
    public void sgtFormulaCars(View v){
        Intent sig = new  Intent(this,FormulaCars.class);
        startActivity(sig);
    }
    public void sgtVintageCars(View v){
        Intent sig = new  Intent(this,VintageCars.class);
        startActivity(sig);
    }
    public void sgtLuxuryCars(View v){
        Intent sig = new  Intent(this,LuxuryCars.class);
        startActivity(sig);
    }
    public void volverAtras(){
        btn_volverAtras.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ant = new Intent(Catalogo.this,MainActivity.class);
                startActivity(ant);
            }
        });


    }

}