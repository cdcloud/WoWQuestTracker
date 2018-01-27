$(function () {

    /**
     * search function
     */
    $("#search").click(function () {
        var character = $("#character").val();
        var realm = $("#realm").val();
        $('#panel-div').empty();


        $.get({
            url: "https://4se9e0g010.execute-api.us-east-1.amazonaws.com/prod/getCompletedQuests",
            dataType: 'html',
            data: {character: character, realm: realm},
            statusCode: {
                200: function (data) {

                    var questCount = 0;
                    $.each(JSON.parse(data), function (quest_line, quest_list) {
                        var unique_quest_id = "quest" + questCount;
                        var template = generateCollapsibleTemplate(quest_line, unique_quest_id);
                        $('#panel-div').append(template);

                        $.each(quest_list, function (qName, status) {
                            var questItem = generateQuestList(qName, status);
                            $('#' + unique_quest_id + ' .panel-body').append(questItem);
                        });
                        questCount += 1;
                    });
                }
            }
        })
    });

    function generateCollapsibleTemplate(quest_line, unique_quest_id) {
        return '<div class="panel panel-default"> \
                            <div class="panel-heading"> \
                                <h4 class="panel-title"> \
                                    <a data-toggle="collapse" data-parent="#panel-div" href="#' + unique_quest_id + '"> \
                                        ' + quest_line + '</a> \
                                </h4> \
                            </div> \
                            <div id="' + unique_quest_id + '" class="panel-collapse collapse"> \
                                <div class="panel-body">    \
                                    <div class="list-group"></div>\
                                </div> \
                             </div> \
                         </div>';
    }

    function generateQuestList(qName, status) {
        return '<a href="#" class="list-group-item list-group-item-' + (status === true ? "success" : "danger") + '">' + qName + '</a>'
    }
});
