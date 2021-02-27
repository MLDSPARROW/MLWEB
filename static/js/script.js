$(document).on('click', '#train_btn', function (e) {
    $.ajax({
        type: "POST",
        url: 'ajax/create-train-model',
        data: {
            'dataset_id': document.getElementById('dataset_id').value,
            'model_name': document.getElementById('ml_model_name').value,
        },
        success: function (response) {
            $('#trained_model_tbl').html(response);
            
        }
    });
});

$(document).on('click', '#predict_btn', function (e) {
    $.ajax({
        type: "GET",
        url: 'ajax/predict-model-data',
        data: {
            'model_id': document.getElementById('model_id').value,
            'input_test_data': document.getElementById('input_test_data').value,
        },
        success: function (response) {
            $("#prediction_result").html(response);
            document.getElementById('prediction_result')
            .scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
            
        },
        error: function (xhr, ajaxOptions, thrownError) {
            let errorMessage = JSON.parse(xhr.responseText);
            $('#trained_model_tbl').html(errorMessage['t']);
            if (errorMessage) {
                toastr.error(errorMessage['error']).attr('style', 'width: 400px !important;height: 70px;font-size: 100%;');
            }
        }
    });
});

function select_dataset_id(id){
    $('#dataset_id').val(id);  
    document.getElementById('selected_ml')
            .scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
}

function select_model_id(id){
    $('#model_id').val(id);    
    document.getElementById('predict_data')
                .scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
}

function select_algorithm_name(name){
    $('#ml_model_name').val(name);  
    document.getElementById('ml_model_name')
                .scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
}