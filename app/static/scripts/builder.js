$(document).ready(function () {

    var builderform = $(".builder-form");
    var currentPart = 0;
    var formParts = $(".form_part").toArray();
    var next = $("#nextbtn");
    var nexthidden = false;
    var back = $("#backbtn");
    var backhidden = true;
    var submitbtn = $("#submit");
    var submitbtnhidden = true;
    var infobtn = $("#class-info-btn");
    var bardbtn = $(".bardbtn");
    var clericbtn = $(".clericbtn");
    var druidbtn = $(".druidbtn");
    var fighterbtn = $(".fighterbtn");
    var paladinbtn = $(".paladinbtn");
    var rangerbtn = $(".rangerbtn");
    var thiefbtn = $(".thiefbtn");
    var wizardbtn = $(".wizardbtn");
    var bard = $(".bard");
    var cleric = $(".cleric");
    var druid = $(".druid");
    var fighter = $(".fighter");
    var paladin = $(".paladin");
    var ranger = $(".ranger");
    var thief = $(".thief");
    var wizard = $(".wizard");
    var info = $(".info");
    var allclassbuttons = $(".class-btn");
    var allclasses = $(".class-name");
    var allclasstext = $(".class-text");
    var currentclasstext = info;
    var classformpart = $(".class-form-part");
    var classcardtext = $(".class-card-text");
    var selectclassbtn = $("#select-class-btn");
    var selectclassbtntext = $("#select-class-btn-text");
    var heroclass = $("#heroclass");
    var herorace = $("#herorace");
    var heroname = $("#heroname");
    var heroalignment = $("#heroalignment");
    var strstat = $("#herostrength");
    var strscore = $("#str-score");
    var strmod = $("#str-mod");
    var dexstat = $("#herodexterity");
    var dexscore = $("#dex-score");
    var dexmod = $("#dex-mod");
    var constat = $("#heroconstitution");
    var conscore = $("#con-score");
    var conmod = $("#con-mod");
    var intstat = $("#herointelligence");
    var intscore = $("#int-score");
    var intmod = $("#int-mod");
    var wisstat = $("#herowisdom");
    var wisscore = $("#wis-score");
    var wismod = $("#wis-mod");
    var chastat = $("#herocharisma");
    var chascore = $("#cha-score");
    var chamod = $("#cha-mod");
    var hpfield = $("#herohp");
    var hpstat = $("#herohp-span");

    // Get current character information
    var previewData = $(".preview_data").toArray();
    var formParts = $(".form_part").toArray();


    // Hide and adjust height of stuff
    $(submitbtn).hide();
    $(back).hide();
    $(next).hide();
    $(builderform).animate({ height: $(formParts[currentPart]).css("height") });

    next.click(function () {
        doNext();
    })

    function doNext() {
        $(formParts[currentPart]).hide("slide", { direction: "left" }, 400);
        // First show the submit button.
        $(submitbtn).show();
        submitbtnhidden = false;
        $(formParts[currentPart + 1]).show("slide", { direction: "right" }, 500);
        currentPart++;
        if (currentPart == formParts.length - 1) {
            // Then hide the next button
            $(next).hide("slide", { direction: "right" }, 400);
            nexthidden = true;
        }
        else {
            $(next).delay(500).show("slide", { direction: "right"}, 500);
        }
        if (backhidden) {
            $(back).delay(500).show("slide", { direction: "left" }, 500);
            backhidden = false;
        }

        //activate next step on progressbar using the index
        $("#progressbar li").eq(currentPart).addClass("active");
        $("#progressbar li").eq(currentPart - 1).children("div").toggle();
        $("#progressbar li").eq(currentPart).children("div").toggle();

        //Update the preview data using current part index
        updatePreviewData();
        $(previewData[currentPart - 1]).show();


        // Adjust the height of the builder-form when loading a new form.
        $(builderform).animate({ height: $(formParts[currentPart]).css("height") });
    }

    back.click(function () {
        doBack();
    })

    function doBack() {
        $(formParts[currentPart]).hide("slide", { direction: "right" }, 400);
        $(formParts[currentPart - 1]).show("slide", { direction: "left" }, 500);
        currentPart--;
        if (currentPart == 0) {
            $(back).hide("slide", { direction: "left" }, 400);
            $(next).hide("slide", { direction: "right" }, 400);
            backhidden = true;
        }
        let delayTimer = 0;
        if (!submitbtnhidden) {
            //$(submitbtn).hide();
            delayTimer = 500;
        }
        if (nexthidden) {
            $(next).delay(delayTimer).show("slide", { direction: "right" }, 500);
            nexthidden = false;
        }

        //activate next step on progressbar using the index of next_fs
        $("#progressbar li").eq(currentPart + 1).removeClass("active");
        $("#progressbar li").eq(currentPart + 1).children("div").toggle();
        $("#progressbar li").eq(currentPart).children("div").toggle();

        // Hide the last preview data part
        $(previewData[currentPart + 1]).hide();
        $(".preview-data-class").show()

        // Adjust the height of the builder-form when loading a new form.
        $(builderform).animate({ height: $(formParts[currentPart]).css("height") });
    }

    infobtn.click(function () {
        oldclass = currentclasstext;
        newclass = info;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.html("Select Info");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(infobtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    })

    bardbtn.click(function () {
        oldclass = currentclasstext;
        newclass = bard;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.removeClass().addClass("select-bard");
        selectclassbtntext.html("Select Bard");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(bardbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });
    clericbtn.click(function () {
        oldclass = currentclasstext;
        newclass = cleric;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.removeClass().addClass("select-cleric");
        selectclassbtntext.html("Select Cleric");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(clericbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });
    druidbtn.click(function () {
        oldclass = currentclasstext;
        newclass = druid;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.removeClass().addClass("select-druid");
        selectclassbtntext.html("Select Druid");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(druidbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });
    fighterbtn.click(function () {
        oldclass = currentclasstext;
        newclass = fighter;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.removeClass().addClass("select-fighter");
        selectclassbtntext.html("Select Fighter");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(fighterbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });
    paladinbtn.click(function () {
        oldclass = currentclasstext;
        newclass = paladin;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.removeClass().addClass("select-paladin");
        selectclassbtntext.html("Select Paladin");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(paladinbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });
    rangerbtn.click(function () {
        oldclass = currentclasstext;
        newclass = ranger;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.removeClass().addClass("select-ranger");
        selectclassbtntext.html("Select Ranger");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(rangerbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });
    thiefbtn.click(function () {
        oldclass = currentclasstext;
        newclass = thief;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }

        selectclassbtntext.removeClass().addClass("select-thief");
        selectclassbtntext.html("Select Thief");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(thiefbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });
    wizardbtn.click(function () {
        oldclass = currentclasstext;
        newclass = wizard;
        isToRight = newclass.parent().index() > oldclass.parent().index();
        let slideout;
        let slidein;
        if (isToRight) {
            slideout = "left";
            slidein = "right";
        }
        else {
            slideout = "right";
            slidein = "left";
        }


        selectclassbtntext.removeClass().addClass("select-wizard");
        selectclassbtntext.html("Select Wizard");

        $(allclassbuttons).css({ "opacity": "0.5" });
        $(wizardbtn).css({ "opacity": "1" });
        $(currentclasstext).hide("slide", { direction: slideout }, 500);
        currentclasstext = newclass;
        $(currentclasstext).show("slide", { direction: slidein }, 500);
        currentclasstext.scrollTop(0);
    });


    selectclassbtn.click(function () {
        var selectedClass;
        var selectedCSSClass;
        var classList = selectclassbtntext.attr('class').split(/\s+/);
        $.each(classList, function (index, item) {
            selectedCSSClass = item;
        });
        switch (selectedCSSClass) {
            case 'select-bard':
                heroclass.val("Bard");
                classChange("bard");
                break;
            case 'select-cleric':
                heroclass.val("Cleric");
                classChange("cleric");
                break;
            case 'select-druid':
                heroclass.val("Druid");
                classChange("druid");
                break;
            case 'select-fighter':
                heroclass.val("Fighter");
                classChange("fighter");
                break;
            case 'select-paladin':
                heroclass.val("Paladin");
                classChange("paladin");
                break;
            case 'select-ranger':
                heroclass.val("Ranger");
                classChange("ranger");
                break;
            case 'select-thief':
                heroclass.val("Thief");
                classChange("thief");
                break;
            case 'select-wizard':
                heroclass.val("Wizard");
                classChange("wizard");
                break;
        }
        doNext();

    });

    // Update modifiers part when stats change.
    strstat.change(function () {
        updateModifiers(strstat, strscore, strmod);
    })
    dexstat.change(function () {
        updateModifiers(dexstat, dexscore, dexmod);
    })
    constat.change(function () {
        updateModifiers(constat, conscore, conmod);
        getData(class_select.value, "hp");
    })
    intstat.change(function () {
        updateModifiers(intstat, intscore, intmod);
    })
    wisstat.change(function () {
        updateModifiers(wisstat, wisscore, wismod);
    })
    chastat.change(function () {
        updateModifiers(chastat, chascore, chamod);
    })

    function updateModifiers(origStat, modStat, modVal) {
        let statscore = parseInt(origStat.val());
        let modscore = "0";
        if ((statscore => 1) && (statscore <= 3)) {
            console.log("statscore is between 1 and 3");
            modscore = "-3";
        }
        else if (statscore >= 4 && statscore <= 5) {
            modscore = "-2";
        }
        else if (statscore >= 6 && statscore <= 8) {
            modscore = "-1";
        }
        else if (statscore >= 9 && statscore <= 12) {
            modscore = "0";
        }
        else if (statscore >= 13 && statscore <= 15) {
            modscore = "+1";
        }
        else if (statscore >= 16 && statscore <= 17) {
            modscore = "+2";
        }
        else if (statscore >= 18) {
            modscore = "+3";
        }
        modStat.html(origStat.val());
        modVal.html(modscore);
    }

    function updatePreviewData() {
        $(".preview-data-class").html(class_select.value);
        $(".preview-data-race").html(race_select.options[race_select.selectedIndex].text);
        $(".preview-data-name").html(heroname.val());
        $(".preview-data-looks").html("Looks");
        $(".preview-data-stats").html("Stats");
        $(".preview-data-modifiers").html("Modifiers");
        $(".preview-data-hp").html(hpfield.val());
        $(".preview-data-moves").html("Moves");
        $(".preview-data-alignment").html(alignment_select.options[alignment_select.selectedIndex].text);
        $(".preview-data-gear").html("Gear");
        $(".preview-data-bonds").html("Bonds");
    }

    $(window).resize(
        function () {
            adjustWidth();
        });
    let class_select = document.getElementById('heroclass');
    let race_select = document.getElementById('herorace');
    let alignment_select = document.getElementById('heroalignment');
    let eyes_select = document.getElementById('heroeyes');
    let hair_select = document.getElementById('herohair');
    let clothing_select = document.getElementById('heroclothing');
    let body_select = document.getElementById('herobody');
    let skin_select = document.getElementById('heroskin');
    let symbol_select = document.getElementById('herosymbol');
    let class_select_btn = document.getElementById('select-class-btn');
    let hp_textfield = document.getElementById('herohp');
    let hp_textstat = document.getElementById('herohp-span');

    class_select.onchange = function () {
        class_name = class_select.value;
        getData(class_name, "race");
        getData(class_name, "alignment");
        getData(class_name, "hp");

        getData(class_name, "looks", "eyes");
        getData(class_name, "looks", "hair");
        getData(class_name, "looks", "clothing");
        getData(class_name, "looks", "body");
        getData(class_name, "looks", "skin");
        getData(class_name, "looks", "symbol");
    }

    function classChange(class_name) {
        getData(class_name, "race");
        getData(class_name, "alignment");
        getData(class_name, "hp");

        getData(class_name, "looks", "eyes");
        getData(class_name, "looks", "hair");
        getData(class_name, "looks", "clothing");
        getData(class_name, "looks", "body");
        getData(class_name, "looks", "skin");
        getData(class_name, "looks", "symbol");
    }

    function getData(class_name, LKUP_type, arg = null) {
        switch (LKUP_type) {
            case 'looks':
                fetch('/looks/' + class_name + '/' + arg).then(function (response) {
                    response.json().then(function (data) {
                        let optionHTML = '<option value></option>';
                        var look_data;
                        var select_box;
                        switch (arg) {
                            case "eyes":
                                look_data = data.eyes;
                                select_box = eyes_select;
                                break;
                            case "hair":
                                look_data = data.hair;
                                select_box = hair_select;
                                break;
                            case "clothing":
                                look_data = data.clothing;
                                select_box = clothing_select;
                                break;
                            case "body":
                                look_data = data.body;
                                select_box = body_select;
                                break;
                            case "skin":
                                look_data = data.skin;
                                select_box = skin_select;
                                break;
                            case "symbol":
                                look_data = data.symbol;
                                select_box = symbol_select;
                                break;
                        }
                        if (look_data.length > 0) {
                            for (var description of look_data) {
                                optionHTML += '<option value="' + description.id + '">' + description.look_details + '</option>';
                            }
                            select_box.innerHTML = optionHTML;
                            select_box.parentElement.style.display = "inline-block";
                        }
                        else {
                            select_box.innerHTML = optionHTML;
                            select_box.parentElement.style.display = "none";
                        }
                    })
                });
                break;
            case 'race':
                fetch('/race/' + class_name).then(function (response) {
                    response.json().then(function (data) {
                        let optionHTML = '<option value></option>';
                        var race_data;
                        var select_box;
                        //race_data = data.race_name;
                        select_box = race_select;
                        $(select_box).empty()
                        race_data = data.race
                        for (var i = 0; i < race_data.length; i++) {
                            //optionHTML += '<option value="' + race_data[i].id + '">' + race_data[i].race_name + '</option>';
                            $(select_box).append(
                                $('<option>', {
                                    value: race_data[i].id,
                                    text: race_data[i].race_name
                                })
                            );
                        }
                        //select_box.innerHTML = optionHTML;
                    })
                });
                break;
            case 'alignment':
                fetch('/alignment/' + class_name).then(function (response) {
                    response.json().then(function (data) {
                        let optionHTML = '<option value></option>';
                        var alignment_data;
                        var select_box;
                        //alignment_data = data.alignment_name;
                        select_box = alignment_select;
                        alignment_data = data.alignment;
                        for (var i = 0; i < alignment_data.length; i++) {
                            optionHTML += '<option value="' + alignment_data[i].id + '">' + alignment_data[i].alignment_name + '</option>';
                        }
                        select_box.innerHTML = optionHTML;
                    })
                });
                break;
            case 'hp':
                fetch('/hp/' + class_name).then(function (response) {
                    response.json().then(function (data) {
                        var hp_data;
                        hp_data = data.hp;
                        console.log("constitution stat: " + typeof(constat.val()))
                        console.log("base_hp: " + typeof(hp_data[0].base_hp))
                        hpfield.val(parseInt(constat.val()) + hp_data[0].base_hp);
                        hpstat.html(parseInt(constat.val()) + hp_data[0].base_hp);
                        return hp_data[0].base_hp;
                    })
                });
                break;
        }
    }
});

function adjustWidth() {
    var windowHeight = $(window).height();
    $(".class-card-text").height()
    var parentwidth = $(".class-card-text").width();
    $(".swipe-content").width(parentwidth);
}

$(function () {
    $("#fixer").click(
        function () {
            toggleFixed();
        });
    $(window).resize(
        function () {
            adjustWidth();
        })
});

var previewhtml = $(".preview-data-form");
//var previewhtml = "<div class='preview-data-form'><p class='preview_data preview-data-class' style='display:none;'></p><p class='preview_data preview-data-race' style='display:none;'></p><p class='preview_data preview-data-name' style='display:none;'></p><p class='preview_data preview-data-looks' style='display:none;'></p><p class='preview_data preview-data-stats' style='display:none;'></p><p class='preview_data preview-data-modifiers' style='display:none;'></p><p class='preview_data preview-data-hp' style='display:none;'></p><p class='preview_data preview-data-moves' style='display:none;'></p><p class='preview_data preview-data-alignment' style='display:none;'></p><p class='preview_data preview-data-gear' style='display:none;'></p><p class='preview_data preview-data-bonds' style='display:none;'></p></div>";

$('#preview-data-button').click(function () {
    previewhtml.show();
    showDialog({

        title: 'Character Info',

        text: previewhtml.html(),

        negative: {

            title: 'Close'

        }

    });
    previewhtml.hide();

});

var statsShowMore = $(".stats-show-more");

$('#stats-show-more-btn').click(function () {
    statsShowMore.show();
    showDialog({

        title: 'Choosing Stats',

        text: statsShowMore.html(),

        negative: {

            title: 'Close'
            
        }
    });
    statsShowMore.hide();
});

var modifiersShowMore = $(".modifiers-show-more");

$('#modifiers-show-more-btn').click(function () {
    modifiersShowMore.show();
    showDialog({

        title: 'More About Modifiers',

        text: modifiersShowMore.html(),

        negative: {

            title: 'Close'
            
        }
    });
    modifiersShowMore.hide();
});