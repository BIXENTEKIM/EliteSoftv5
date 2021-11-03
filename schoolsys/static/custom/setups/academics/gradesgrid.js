
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    gradesgridModal();
    getGradesgrids();
    saveGradesgrid();
    editGradesgrid();
    deleteGradesgrid();
    searchDepartment();
    departmentChange();
})
function gradesgridModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#gradesgridModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#department-frm').empty();
      $('#department-code').val('');
      $('#gradesgrid-form')[0].reset();
      $('#grades_code').val('');
}
function deleteGradesgrid() {
    $('#gradesgridTable').on('click','.btn-deleteGradesgrid',function (s) {
        var data = $(this).closest('tr').find('#delete-gradesgrid').val();
        bootbox.confirm("Are you sure want to delete this Grades?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteGradesgrid/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getGradesgrids()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getGradesgrids() {
     $.ajax({
        type: 'GET',
        url: 'getGradesgrids',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#gradesgridTable').DataTable().destroy();
       $("#gradesgridTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#gradesgridTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.grades_val1 + "</td>"
                    + "<td>" + item.grades_val2 + "</td>"
                    + "<td>" + item.grades_grade + "</td>"
                    + "<td>" + item.grades_remarks + "</td>"
                    + "<td>" + item.gradesgridDepartment + "</td>"
                    + "<td>" + item.grades_option + "</td>"
                    + "<td>" + '<form id="editGradesgrid" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-gradesgrid" name="id" value=' + item.grades_code + '></form><button class="btn btn-outline-primary btn-sm btn-editGradesgrid" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteGradesgrid" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-gradesgrid" name="id" value=' + item.grades_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteGradesgrid" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#gradesgridTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveGradesgrid(){
    $('#saveGradesgrid').click(function () {
        var data=$('#gradesgrid-form').serialize();
        var url = '';
        if($('#grades_code').val()===''){
          url = 'createGradesgrid'
        }else{
            url = 'updateGradesgrid/'+$('#grades_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getGradesgrids()
            clearData()
            $('#gradesgridModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editGradesgrid(){
    $('#gradesgridTable').on('click','.btn-editGradesgrid',function (s) {
        var data=$(this).closest('tr').find('#edit-gradesgrid').val();
        $.ajax({
            type: 'GET',
            url: 'editGradesgrid/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#grades_code').val(s.grades_code);
            $('#grades_val1').val(s.grades_val1);
            $('#grades_val2').val(s.grades_val2);
            $('#grades_grade').val(s.grades_grade);
            $('#grades_remarks').val(s.grades_remarks);
            $('#grades_option').val(s.grades_option);


            if (s.gradesgridDepartmentCode) {
                $('#department-code').val(s.gradesgridDepartmentCode)

                var $newOption = $("<option selected='selected' value='" + s.gradesgridDepartmentCode + "'>'+s.gradesgridDepartmentName+'</option>").val(s.gradesgridDepartmentCode.toString()).text(s.gradesgridDepartmentName)

                $('#department-frm').append($newOption).trigger('change');
            } else {
                $('#department-code').val('')

                $('#department-frm').empty();

            }

        $('#gradesgridModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
function searchDepartment() {
     $('#department-frm').select2({
           placeholder: 'Departments',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchDepartment',
             data: function (params) {
                 console.log("AA", params);
                 return {
                     query: params.term,
                     gotoPage: params.page
                 }
             },

             processResults: function (data,params) {
                 params.page = params.page || 1;
                 console.log('data: ', data);
                 return {
                   results: data.results
                 };
             }

         }
     })
}

function departmentChange(){
    $('#department-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#department-code').val(data.id)
    $('#department-name').val(data.text)

});
    $("#department-frm").on("select2:unselecting", function(e) {
    $('#department-code').val('')
    $('#department-name').val('')
 });
}

