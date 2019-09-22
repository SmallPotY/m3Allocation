package com.smallpot.m3;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Insets;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.smallpot.m3.utils.http.HttpUtil;

import org.w3c.dom.Text;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    Button btnAllocation;
    Button btnEmbarkation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        btnAllocation = findViewById(R.id.btnAllocation);
        btnAllocation.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this,AllocationActivity.class);
                startActivity(intent);

            }
        });

//        btnTest.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                HttpUtil http = new HttpUtil( "http://192.168.1.104:8888/");
//                http.post("",new okhttp3.Callback(){
//                    @Override
//                    public void onFailure(Call call, IOException e) {
//                        Log.d("err", "onFailure: err");
//                    }
//
//                    @Override
//                    public void onResponse(Call call, Response response) throws IOException {
//                        Log.d("ok", response.body().string());
//
//                    }
//                });
//            }
//        });

    }
}
