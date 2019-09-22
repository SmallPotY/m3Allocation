package com.smallpot.m3.utils.http;

import java.net.URL;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import okhttp3.Call;
import okhttp3.FormBody;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;

public class HttpUtil {

    private  String url;
    private  OkHttpClient client;

    public HttpUtil(String _url){
        client = new OkHttpClient();
        url = _url;
    }

    public  void post(String json, okhttp3.Callback callback){

        MediaType JSON = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(JSON, json);

        Request request = new Request.Builder().
                url(url)
                .post(body)
                .build();

        client.newCall(request).enqueue(callback);
    }
}
